from manim import *
from manim_editor import PresentationSectionType
from utils import elbow_arrow, labelled_block
from math import sqrt


class WhileLoopFlowChart(Scene):

    def construct(self):
        entry_block = labelled_block("Loop Entry", 1, 2).shift(UP * 3)

        condition_block = labelled_block("Loop Condition", 2, 2, rotate=PI / 4)
        body_block = labelled_block("Body", 1, 2).shift(DOWN * 3)

        entry_arrow = Arrow(start=entry_block.get_bottom(), end=condition_block.get_top(), buff=0)

        true_arrow = Arrow(
            start=condition_block.get_bottom(), end=body_block.get_top(), buff=0
        )

        loop_arrow = elbow_arrow(body_block.get_left(), condition_block.get_left(), -1)

        exit_block = labelled_block("Loop Exit", 1, 2).shift(RIGHT * 4)

        exit_arrow = Arrow(
            start=condition_block.get_right(), end=exit_block.get_left(), buff=0
        )

        true_label = Text("True", font_size=24).shift(true_arrow.get_right() + RIGHT * 0.4)
        false_label = Text("False", font_size=24).shift(exit_arrow.get_top() + UP * 0.2)


        self.play(Create(entry_block))
        self.play(Create(condition_block))
        self.play(Create(body_block))
        self.play(Create(exit_block))

        self.play(Create(entry_arrow))
        self.play(Create(true_arrow), Create(true_label))
        self.play(Create(loop_arrow))
        self.play(Create(exit_arrow), Create(false_label))

        self.add(
            condition_block, body_block, true_arrow, loop_arrow, exit_block, exit_arrow, true_label, false_label, entry_block, entry_arrow)

        self.pause(2)