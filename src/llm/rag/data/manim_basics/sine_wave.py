from manim import *
import numpy as np

# Example: Sine Wave
class SineWaveScene(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7,
            y_length=4,
            axis_config={"color": WHITE},
        )

        # Define sine function
        sine_curve = axes.plot(lambda x: np.sin(x), color=BLUE, stroke_width=3)

        # Label axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Animate
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(sine_curve))
        self.wait(2)
