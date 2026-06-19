from copy import deepcopy
from functools import reduce

class Expr:
    pass

class Tensor(Expr):
    def __init__(self, name: str, indicies: tuple[str, ...]) -> None:
        self.name = name
        self.indicies = indicies

    def nind(self):
        return len(self.indicies)
    
    def has_index(self, index: str):

        return index in self.indicies

    def rename(self, old_index: str, new_index: str):

        assert old_index in self.indicies
        assert new_index not in self.indicies

        self.indicies = tuple(
            [new_index if c == old_index else c for c in self.indicies]
        )

    def copy(self):
        return deepcopy(self)
    
class TensorAddition(Tensor):
    def __init__(self, name: str, *tensors: Tensor) -> None:
        pass


class TensorContraction(Tensor):
    def __init__(self, name: str, *tensors: Tensor) -> None:
        contraction_indicies = []

        indicies = []
        tensor_index_count = dict()

        for t in tensors:
            for ind in t.indicies:
                tensor_index_count[ind] = tensor_index_count.get(ind, 0) + 1
                assert tensor_index_count[ind] <= 2

        for t in tensors:
            for ind in t.indicies:
                if tensor_index_count[ind] > 1:
                    contraction_indicies.append(ind)
                else:
                    indicies.append(ind)

        super().__init__(name, tuple(indicies))

        self.tensors: tuple[Tensor, ...] = tensors
        self.contraction_indicies = contraction_indicies

    def rename(self, old_index: str, new_index: str):
        super().rename(old_index, new_index)

        for t in self.tensors:
            t.rename(old_index, new_index)
    
    def _tensors_iterator(self):
        pass


class KroneckerDelta(Tensor):
    def __init__(self, a: str, b: str) -> None:
        super().__init__("d", (a, b))

    def apply(self, tensor: Tensor):

        if isinstance(tensor, TensorContraction):
            return reduce(lambda accum, x: accum or x, map(self.apply, tensor.tensors))
        elif isinstance(tensor, TensorAddition):
            pass
        elif isinstance(tensor, Tensor):
            a, b = self.indicies
            if tensor.has_index(a):
                tensor.rename(a, b)
                return True
            elif tensor.has_index(b):
                tensor.rename(b, a)
                return True
            else:
                return False

    def __mul__(self, other: Tensor):

        if isinstance(other, TensorContraction):
            pass

        
if __name__ == "__main__":

    KroneckerDelta("i", "j") * KroneckerDelta("j", "k")
