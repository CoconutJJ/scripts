from manim import *

class Base16Explanation(Scene):

    def construct(self):

        base10_symbols = Text("Base 10: 0-9").shift(UP)
        base16_symbols = Text("Base 16: 0-9, A-F")      

        b10_number = Text("1269").shift(UP)
        b16_number = Text("4F5")

        self.add(base16_symbols, base10_symbols)

        self.play(Transform(base10_symbols, b10_number))
        self.pause(1)
        self.play(Transform(base16_symbols, b16_number))
        self.pause(1)

        b16_expanded = MathTex("4 \cdot 16^2 + F \cdot 16^1 + 5 \cdot 16^0 = 1269").shift(DOWN)
        self.play(Write(b16_expanded))
        self.pause(1)

