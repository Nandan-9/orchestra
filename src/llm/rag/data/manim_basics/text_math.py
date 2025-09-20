from manim import *


# Example 1: Simple Text
class TextScene(Scene):
    def construct(self):
        text = Text("Hello, Manim!", font_size=72, color=BLUE)
        self.play(Write(text))
        self.wait(2)


# Example 2: Math Expression
class MathScene(Scene):
    def construct(self):
        math_expr = MathTex(r"E = mc^2", font_size=96, color=YELLOW)
        self.play(Write(math_expr))
        self.wait(2)


# Example 3: Mixed Text + Math
class MixedScene(Scene):
    def construct(self):
        text = Text("Famous Formula:", font_size=48)
        math_expr = MathTex(r"\int_a^b f(x) \, dx", font_size=72, color=GREEN).next_to(text, DOWN)

        self.play(Write(text))
        self.play(Write(math_expr))
        self.wait(2)
