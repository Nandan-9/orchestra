from manim import *

# Example 1: FadeIn / FadeOut
class FadeScene(Scene):
    def construct(self):
        text = Text("Fade In and Out", font_size=72, color=BLUE)
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

# Example 2: GrowFromCenter / ShrinkToCenter
class GrowShrinkScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=RED)
        self.play(GrowFromCenter(circle))
        self.wait(1)
        self.play(ShrinkToCenter(circle))
        self.wait(1)

# Example 3: Write / Unwrite (for text or math)
class WriteScene(Scene):
    def construct(self):
        text = Text("Writing Animation", font_size=72, color=GREEN)
        math_expr = MathTex(r"E = mc^2", font_size=96, color=YELLOW).next_to(text, DOWN)
        self.play(Write(text))
        self.play(Write(math_expr))
        self.wait(2)

# Example 4: Transform / ReplacementTransform
class TransformScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle, square))
        self.wait(1)

# Example 5: Rotations and Shifts
class RotateShiftScene(Scene):
    def construct(self):
        triangle = Triangle(color=PURPLE)
        self.play(Create(triangle))
        self.play(triangle.animate.rotate(PI/4))
        self.play(triangle.animate.shift(RIGHT*2 + UP*1))
        self.wait(1)
