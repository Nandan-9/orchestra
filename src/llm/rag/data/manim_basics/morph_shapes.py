from manim import *

class MorphingScene(Scene):
    def construct(self):
        # Example 1: Circle -> Square
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        self.play(Create(circle))
        self.wait(0.5)
        self.play(Transform(circle, square))  # Morph circle into square
        self.wait(1)

        # Example 2: Text morph
        text1 = Text("Hello", font_size=72, color=GREEN)
        text2 = Text("World!", font_size=72, color=YELLOW)
        self.play(Write(text1))
        self.wait(0.5)
        self.play(Transform(text1, text2))  # Morph text1 into text2
        self.wait(1)

        # Example 3: MathTex morph
        math1 = MathTex(r"a^2 + b^2", font_size=72, color=BLUE)
        math2 = MathTex(r"c^2", font_size=72, color=RED)
        self.play(Write(math1))
        self.wait(0.5)
        self.play(Transform(math1, math2))  # Morph one math expression into another
        self.wait(1)

        # Example 4: ReplacementTransform (fade out old, fade in new)
        circle2 = Circle(color=PURPLE)
        square2 = Square(color=ORANGE)
        self.play(Create(circle2))
        self.wait(0.5)
        self.play(ReplacementTransform(circle2, square2))  # Circle disappears, square appears
        self.wait(1)
