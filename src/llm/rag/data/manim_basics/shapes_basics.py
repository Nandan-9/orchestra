from manim import *

# Example 1: Circle
class CircleScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.play(Create(circle))
        self.wait(2)

# Example 2: Square
class SquareScene(Scene):
    def construct(self):
        square = Square(side_length=2, color=RED)
        self.play(Create(square))
        self.wait(2)

# Example 3: Triangle
class TriangleScene(Scene):
    def construct(self):
        triangle = Triangle().scale(2).set_color(GREEN)
        self.play(Create(triangle))
        self.wait(2)

# Example 4: Axes + Dot
class AxesScene(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-2, 2])
        dot = Dot(point=axes.c2p(1, 1), color=YELLOW)
        self.play(Create(axes), FadeIn(dot))
        self.wait(2)
