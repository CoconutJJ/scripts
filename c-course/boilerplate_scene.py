from manim import *
from manim_editor import PresentationSectionType
from utils import remove_dot_objs
class Boilerplate(Scene):

    def construct(self):

        self.next_section(PresentationSectionType.NORMAL)
        codeblock = Code("examples/boilerplate.c", style="default")
        label = Text("C")
        self.play(Create(label))

        self.next_section(PresentationSectionType.NORMAL)
        self.play(Create(codeblock))

        self.next_section(PresentationSectionType.NORMAL)

        r1 = SurroundingRectangle(remove_dot_objs(codeblock.code[3]), color=GREEN)
        r2 = SurroundingRectangle(remove_dot_objs(codeblock.code[7]), color=GREEN)

        self.play(Create(r1), Create(r2))

        self.next_section(PresentationSectionType.NORMAL)
        
        codeblock_2 = Code("examples/hello_world.c", style="default")
        self.remove(r1, r2)
        self.play(Transform(codeblock, codeblock_2))

        line = remove_dot_objs(codeblock_2.code[5])
        self.next_section(PresentationSectionType.NORMAL)
        quote_rect = SurroundingRectangle(line[7], color=GREEN)
        endquote_rect = SurroundingRectangle(line[19], color=GREEN)
        semicolon_rect = SurroundingRectangle(line[21], color=GREEN)
        self.next_section(PresentationSectionType.NORMAL)
        self.play(Create(quote_rect), Create(endquote_rect))
        self.next_section(PresentationSectionType.NORMAL)
        self.play(Create(semicolon_rect))