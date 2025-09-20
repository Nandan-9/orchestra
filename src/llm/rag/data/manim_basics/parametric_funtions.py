from manim import *
import numpy as np

# Example: Parametric Function (Circle)
class ParametricScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )

        # Parametric circle: x = cos(t), y = sin(t)
        param_curve = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 2*PI],
            color=BLUE,
            stroke_width=3
        )

        # Animate
        self.play(Create(axes))
        self.play(Create(param_curve))
        self.wait(2)

# Example 2: Lissajous Curve
class LissajousScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        )

        lissajous = axes.plot_parametric_curve(
            lambda t: np.array([np.sin(3*t), np.sin(2*t), 0]),
            t_range=[0, 2*PI],
            color=YELLOW,
            stroke_width=3
        )

        self.play(Create(axes))
        self.play(Create(lissajous))
        self.wait(2)
