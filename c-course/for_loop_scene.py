from manim import *
from manim_editor import PresentationSectionType
from math import sqrt
from utils import elbow_arrow
class ForLoopFlowChart(Scene):

    def chart_block(self, text: str) -> VGroup:
        blk = Rectangle(height=1, width=2)
        txt = Text(text).scale(0.5)
        txt.move_to(blk.get_center())

        grp = VGroup()
        grp.add(blk, txt)

        return grp

    def condition_block(self, text: str) -> VGroup:
        blk = Rectangle(height=sqrt(2) + 0.2, width=sqrt(2) + 0.2).rotate(PI/4)
        txt = Text(text).scale(0.4)
        txt.move_to(blk.get_center())

        grp = VGroup()
        grp.add(blk, txt)

        return grp

    def construct(self):

        initializer = self.chart_block("Initializer").shift(UP * 3)
        condition = self.condition_block("Loop Condition")
        body = self.chart_block("Loop Body").shift(LEFT * 4)
        update = self.chart_block("Update").shift(LEFT * 4 + DOWN * 2)
        exit_blk = self.chart_block("Exit").shift(DOWN * 3.5)
        
        arrows = [
            Arrow(start=initializer.get_bottom(), end=condition.get_top(), buff=0),
            t := Arrow(start=condition.get_left(), end=body.get_right(), buff=0),
            Text("True").move_to(t.get_top() + UP * 0.3).scale(0.5),
            f := elbow_arrow(condition.get_right(), exit_blk.get_right()),
            Text("False").move_to(f.get_right() + RIGHT * 0.5).scale(0.5),
            Arrow(start=body.get_bottom(), end=update.get_top(), buff=0),
            elbow_arrow(update.get_right(), condition.get_bottom(), width=0)
        ]

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(initializer))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(condition))
        
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(update))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(body))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(exit_blk))
        
        for p in arrows:
            self.next_section(type=PresentationSectionType.NORMAL)
            self.play(Create(p))
        
    
