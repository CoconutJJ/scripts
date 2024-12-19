from manim import *
from manim_editor import PresentationSectionType
from utils import remove_dot_objs

class StackVariableAllocation(Scene):

    def variable_block(self, name: str, height: int, font_size=24):

        blk = Rectangle(height=height, width=2)
        label = Text(name, font_size=font_size).shift(blk.get_center())
        vg = VGroup()
        vg.add(blk, label)

        return vg


    def construct(self):
        mem = Rectangle(height=7, width=2).shift(RIGHT * 5)

        code_block = Code("examples/memory_model.c", line_spacing=1)
        code_block.shift(LEFT * 3)

        x_highlight = SurroundingRectangle(remove_dot_objs(code_block.code[2]))
        y_highlight = SurroundingRectangle(remove_dot_objs(code_block.code[4]))

        v1 = self.variable_block("age", 1).shift(UP * 3 + RIGHT * 2)

        v2 = self.variable_block("temperature", 1.5)
        v2.shift(v1.get_bottom() + v2.height / 2 * DOWN)

        self.add(mem, code_block)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(x_highlight))
        self.play(Create(v1))
        self.play(v1.animate.shift(RIGHT * 3))
        self.next_section(type=PresentationSectionType.NORMAL)

        self.play(Transform(x_highlight, y_highlight))
        self.play(Create(v2))
        self.play(v2.animate.shift(RIGHT * 3))
        self.next_section(type=PresentationSectionType.NORMAL)

        low_addr = Text("0x0000", font_size=24)
        low_addr.shift(
            mem.get_bottom() + LEFT * (mem.width / 2 + low_addr.width / 2 + 0.2)
        )

        high_addr = Text("0x...", font_size=24)
        high_addr.shift(
            mem.get_top() + LEFT * (mem.width / 2 + high_addr.width / 2 + 0.2)
        )
        self.next_section(type=PresentationSectionType.NORMAL)

        self.play(Create(low_addr), Create(high_addr))
