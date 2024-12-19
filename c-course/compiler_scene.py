from manim import *
from utils import labelled_block
class CompilerScene(Scene):

    def construct(self):
        source_file = labelled_block("Source .c \nFile", height=2, width=2).shift(LEFT * 5)
        compiler_block = labelled_block("Compiler", height=1, width=2).shift(LEFT * 2)

        object_file = labelled_block("Object File \n*.o", height=2, width=2).shift(RIGHT)
        
        linker = labelled_block("Linker", height=1, width=2).shift(RIGHT * 4)

        arr2 = Arrow(start=compiler_block.get_right(), end=object_file.get_left(), buff=0)
        arr3 = Arrow(start=object_file.get_right(), end=linker.get_left(), buff=0)
        executable_file = Text("a.out", font_size=24).shift(RIGHT * 6)
        arr4 = Arrow(start=linker.get_right(), end=executable_file.get_left(), buff=0.1)


        gcc_grp = VGroup()
        gcc_grp.add(compiler_block, object_file, linker, arr2, arr3)
        arr1 = Arrow(start=source_file.get_right(), end=gcc_grp.get_left(), buff=0)
        gcc_block =VGroup(SurroundingRectangle(gcc_grp))
        gcc_block.add(Text("GCC").shift(gcc_block.get_center())) 
        self.add(source_file)
        self.add(gcc_block, arr1, arr4, executable_file)
        self.pause(1)
        self.play(Transform(gcc_block, gcc_grp))

        self.pause(3)


