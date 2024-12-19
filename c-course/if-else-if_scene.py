from manim import *
from utils import labelled_block, elbow_arrow


class IfElseIf(Scene):

    def construct(self):

        c1 = labelled_block("Condition 1", 2, 2, rotate=PI / 4).shift(LEFT * 4 + UP * 2)
        c2 = labelled_block("Condition 2", 2, 2, rotate=PI / 4).shift(UP * 2)
        c3 = labelled_block("Condition 3", 2, 2, rotate=PI / 4).shift(
            RIGHT * 4 + UP * 2
        )

        c1_c2 = Arrow(start=c1.get_right(), end=c2.get_left(), buff=0)
        c2_c3 = Arrow(start=c2.get_right(), end=c3.get_left(), buff=0)

        c1_body = labelled_block("Body", 1, 2).shift(LEFT * 4 + DOWN)
        c2_body = labelled_block("Body", 1, 2).shift(DOWN)
        c3_body = labelled_block("Body", 1, 2).shift(RIGHT * 4 + DOWN)

        c1_body_arrow = Arrow(start=c1.get_bottom(), end=c1_body.get_top(), buff=0)
        c2_body_arrow = Arrow(start=c2.get_bottom(), end=c2_body.get_top(), buff=0)
        c3_body_arrow = Arrow(start=c3.get_bottom(), end=c3_body.get_top(), buff=0)

        exit_blk = labelled_block("Exit", 1, 2).shift(DOWN * 3)

        c1_exit = elbow_arrow(c1_body.get_bottom(), exit_blk.get_left(), width=-3)
        c2_exit = Arrow(c2_body.get_bottom(), exit_blk.get_top(), buff=0)
        c3_exit = elbow_arrow(c3_body.get_bottom(), exit_blk.get_right(), width=3)

        s1 = VGroup(
            c1,
            c2,
            c3,
            c1_c2,
            c2_c3,
            c1_body,
            c2_body,
            c3_body,
            c1_body_arrow,
            c2_body_arrow,
            c3_body_arrow,
            exit_blk,
            c1_exit,
            c2_exit,
            c3_exit,
        )


        self.play(Create(s1, run_time=2))

        self.pause(1)

        self.play(s1.animate.scale(0.75).shift(LEFT * 2))

        cn = labelled_block("Condition N", 2, 2, rotate=PI /4).scale(0.75).shift(c3.get_right() + RIGHT * 2.5)
        
        cn_body = labelled_block("Body", 1, 2).shift(cn.get_bottom() + DOWN * 1.23).scale(0.75)
        
        cn_body_arrow = Arrow(start=cn.get_bottom(), end=cn_body.get_top(), buff=0)
        cn_exit= elbow_arrow(start=cn_body.get_bottom(), end=exit_blk.get_right(), width=6)
        ellipsis = Text(". . .").shift(cn.get_left() + LEFT * 0.75)
        
        self.play(Create(cn), Create(cn_body), Create(cn_body_arrow), Create(cn_exit), Create(ellipsis))
        
        self.pause(2)
        pass
