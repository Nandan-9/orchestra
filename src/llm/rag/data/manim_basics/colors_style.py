from manim import *

# Example 1: Colored Text
class ColoredTextScene(Scene):
    def construct(self):
        text = Text("Colored Text!", font_size=72, color=BLUE)
        self.play(Write(text))
        self.wait(2)

# Example 2: Gradient Text
class GradientTextScene(Scene):
    def construct(self):
        gradient_text = Text(
            "Gradient Text", font_size=72
        ).set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Write(gradient_text))
        self.wait(2)

# Example 3: Styled Math
class StyledMathScene(Scene):
    def construct(self):
        math_expr = MathTex(
            r"a^2 + b^2 = c^2", font_size=96
        )
        math_expr.set_color_by_tex("a", RED)
        math_expr.set_color_by_tex("b", GREEN)
        math_expr.set_color_by_tex("c", BLUE)
        self.play(Write(math_expr))
        self.wait(2)

# Example 4: Background + Shadow Style
class StyledShapeScene(Scene):
    def construct(self):
        square = Square(side_length=2, fill_color=YELLOW, fill_opacity=0.5, color=RED)
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5, color=WHITE).next_to(square, RIGHT, buff=1)
        self.play(FadeIn(square), FadeIn(circle))
        self.wait(2)
