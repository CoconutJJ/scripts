from manim import *
from manim_editor import PresentationSectionType
from utils import elbow_arrow, labelled_block
from math import sqrt


class DoWhileLoopFlowChart(Scene):

    def construct(self):
        entry_block = labelled_block("Loop Entry", 1, 2).shift(UP * 3)

        condition_block = labelled_block("Loop Condition", 2, 2, rotate=PI / 4).shift(
            DOWN * 2
        )
        body_block = labelled_block("Body", 1, 2).shift(UP)

        entry_arrow = Arrow(
            start=entry_block.get_bottom(), end=body_block.get_top(), buff=0
        )

        condition_arrow = Arrow(
            start=body_block.get_bottom(), end=condition_block.get_top(), buff=0
        )
        loop_arrow = elbow_arrow(condition_block.get_left(), body_block.get_left(), -1)

        exit_block = labelled_block("Loop Exit", 1, 2).shift(RIGHT * 4 + DOWN * 2)

        exit_arrow = Arrow(
            start=condition_block.get_right(), end=exit_block.get_left(), buff=0
        )

        true_label = Text("True", font_size=24).shift(
            loop_arrow.get_left() + LEFT * 0.4
        )
        false_label = Text("False", font_size=24).shift(exit_arrow.get_top() + UP * 0.2)

        self.play(Create(entry_block))
        self.play(Create(body_block))
        self.play(Create(condition_block))
        self.play(Create(exit_block))

        self.play(Create(entry_arrow))
        self.play(Create(condition_arrow))
        self.play(Create(loop_arrow), Create(true_label))
        self.play(Create(exit_arrow), Create(false_label))

        # self.add(
        #     condition_block, body_block, loop_arrow, exit_block, exit_arrow, true_label, false_label, entry_block, entry_arrow, condition_arrow)

        self.pause(2)
