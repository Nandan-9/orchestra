from manim import *
import numpy as np

class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"include_numbers": False}
        )
        
        x_labels = VGroup()
        positions = [PI / 2, PI, 3 * PI / 2, 2 * PI]
        labels = [MathTex(r"\frac{\pi}{2}"), MathTex(r"\pi"), MathTex(r"\frac{3\pi}{2}"), MathTex(r"2\pi")]
        for pos, label in zip(positions, labels):
            label.next_to(axes.c2p(pos, 0), DOWN)
            x_labels.add(label)
        
        sine_curve = axes.plot(lambda x: np.sin(x), color=YELLOW)
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        
        self.play(Create(axes), Write(x_labels))
        self.play(Create(sine_curve), MoveAlongPath(dot, sine_curve), run_time=4)
        
        end_dot = Dot(axes.c2p(2 * PI, 0), color=GREEN)
        end_label = MathTex(r"(2\pi, 0)").next_to(end_dot, UP)
        self.play(FadeIn(end_dot), Write(end_label))
        self.wait(2)