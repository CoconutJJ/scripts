from manim import *
from utils import labelled_block

# ruff: noqa: F405

class PointerVariable(VMobject):

    def __init__(self, label: str, height: int, width: int, **kwargs):
        super().__init__(**kwargs)
        self.label = label
        self.variable_block = Rectangle(height=height, width=width)
        self.text_block = Text(label).shift(self.variable_block.get_center())
        self.arrow = None
        self.group = VGroup(self.variable_block, self.text_block)
        self.add(self.group)

    def points_to(self, position) -> AnimationGroup:
        if self.arrow is None:
            self.arrow = Arrow(self.variable_block.get_bottom(), position, buff=0)
            return AnimationGroup(Create(self.arrow))
        else:
            new_arrow = Arrow(self.variable_block.get_bottom(), position, buff=0)
            return AnimationGroup(Transform(self.arrow, new_arrow))

    def indicate(self) -> Animation:
        return Indicate(self.group)

    def arrow_color(self, color) -> AnimationGroup:
        return AnimationGroup(FadeToColor(self.arrow, color))

    def deref(self, level: int = 1) -> AnimationGroup:
        self.save_state()
        return AnimationGroup(
            Transform(
                self.text_block,
                Text("*" * level + self.label).shift(self.text_block.get_center()),
            )
        )

    def clear_deref(self) -> AnimationGroup:
        return AnimationGroup(Restore(self))


class LinkedListNode(VMobject):

    def __init__(self, label: int, height: int, width: int, **kwargs):
        super().__init__(**kwargs)
        self.label = label
        self.value_block = Rectangle(height=height / 2, width=width)
        self.pointer_block = Rectangle(height=height / 2, width=width).shift(
            DOWN * height / 2
        )
        self.label_text = Text(str(label)).shift(self.value_block.get_center())
        self.arrow = None
        self.add(self.value_block, self.pointer_block, self.label_text)

    def __gt__(self, other: "LinkedListNode"):

        return self.points_to(other.get_left())

    def __lt__(self, other: "LinkedListNode"):

        return other.points_to(self.get_left())

    def indicate(self) -> Animation:

        return Indicate(self)

    def points_to(self, position) -> AnimationGroup:
        if self.arrow is None:
            self.arrow = Arrow(self.get_pointer_block_location(), position, buff=0)
            return AnimationGroup(Create(self.arrow))
        else:
            new_arrow = Arrow(self.get_pointer_block_location(), position, buff=0)
            return AnimationGroup(Transform(self.arrow, new_arrow))

    def arrow_color(self, color) -> AnimationGroup:

        return AnimationGroup(FadeToColor(self.arrow, color))

    def clear_arrow(self) -> AnimationGroup:
        return AnimationGroup(FadeOut(self.arrow))

    def get_pointer_block_location(self):

        return self.pointer_block.get_center()


class LinkedList(VMobject):

    def __init__(self, labels: list[int], height: int, width: int, **kwargs):
        super().__init__(**kwargs)

        self.ll_nodes = []

        for s in labels:
            self.ll_nodes.append(LinkedListNode(s, height, width, **kwargs))

        for i, obj in enumerate(self.ll_nodes):

            obj.shift(RIGHT * (-4 + i * (width + 1)))
            self.add(obj)

    def __iter__(self):

        for n in self.ll_nodes:
            yield n

    def __getitem__(self, value):
        return self.ll_nodes[value]

    def render_nodes(self) -> AnimationGroup:

        return AnimationGroup(*[Create(r) for r in self.ll_nodes])

    def link_nodes(self) -> AnimationGroup:

        return AnimationGroup(
            *[s > t for s, t in zip(self.ll_nodes, self.ll_nodes[1:])]
        )

    def get_node(self, index) -> LinkedListNode:
        return self.ll_nodes[index]


class LinkedListScene(Scene):

    def construct(self):

        p = PointerVariable("list", 1, 2).shift(UP * 2 + LEFT * 3)

        l = LinkedList([1, 3, 9, 10], 1, 2)

        node = LinkedListNode(7, 1, 2).shift(UP * 3 + RIGHT * 0.5)

        self.play(l.render_nodes())
        self.play(l.link_nodes())
        self.play(Write(p), Write(node))

        for s, t in zip(l, l[1:]):
            self.play(p.points_to(s.get_pointer_block_location()))
            self.play(s.indicate())
            self.play(t.indicate())
            if s.label < node.label < t.label:
                self.play(p.arrow_color(GREEN))
                self.play(p.deref())
                self.play(s.arrow_color(GREEN))
                self.play(p.points_to(t.get_left()))
                self.play(s.arrow_color(WHITE))
                self.pause(1)
                self.play(p.indicate())
                self.play(node > t)
                self.play(p.clear_deref())
                self.play(p.points_to(s.get_pointer_block_location()))
                self.play(p.arrow_color(RED), s.arrow_color(YELLOW), p.deref())
                self.pause(1)
                self.play(s > node, p.indicate())
                self.play(p.arrow_color(WHITE), s.arrow_color(WHITE), p.clear_deref())
                break
            
