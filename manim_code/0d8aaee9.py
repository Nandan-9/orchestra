import numpy as np
from manim import *

class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"include_numbers": False},
            x_length=10,
            y_length=6
        )
        axis_labels = axes.get_axis_labels("x", "y")
        
        key_points = [np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
        x_labels = VGroup()
        for x_val in key_points:
            if x_val == np.pi:
                tex = "\\pi"
            elif x_val == 2 * np.pi:
                tex = "2\\pi"
            elif x_val == np.pi / 2:
                tex = "\\frac{\\pi}{2}"
            else:
                tex = "\\frac{3\\pi}{2}"
            label = MathTex(tex, font_size=24).next_to(axes.c2p(x_val, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        sine_curve = axes.plot(np.sin, x_range=[0, 2 * np.pi], color=BLUE)
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        
        self.add(axes, axis_labels, x_labels)
        self.play(Create(sine_curve), MoveAlongPath(dot, sine_curve), run_time=4)
        
        end_dot = Dot(color=GREEN).move_to(axes.c2p(2 * np.pi, 0))
        end_label = MathTex("(2\\pi, 0)", font_size=24).next_to(end_dot, DOWN, buff=0.2)
        self.play(ReplacementTransform(dot, end_dot), Write(end_label))
        self.wait()