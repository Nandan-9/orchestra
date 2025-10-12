import numpy as np
from manim import *

class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE}
        )
        axes_labels = axes.get_axis_labels("x", "y")
        
        x_ticks = [PI / 2, PI, 3 * PI / 2, 2 * PI]
        x_labels = VGroup()
        for tick in x_ticks:
            label = MathTex(
                f"{ {PI/2: '\\pi/2', PI: '\\pi', 3*PI/2: '3\\pi/2', 2*PI: '2\\pi'}[tick] }",
                font_size=24
            ).next_to(axes.c2p(tick, 0), DOWN)
            x_labels.add(label)
        
        sine_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        
        tracker = ValueTracker(0)
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        dot.add_updater(lambda d: d.move_to(axes.i2gp(tracker.get_value(), sine_graph)))
        
        self.add(axes, axes_labels, x_labels)
        self.play(
            Create(sine_graph),
            UpdateFromTracker(dot, tracker),
            tracker.animate.set_value(2 * PI),
            run_time=5,
            rate_func=linear
        )
        dot.clear_updaters()
        
        end_dot = Dot(axes.c2p(2 * PI, 0), color=GREEN)
        end_label = MathTex("(2\\pi, 0)", font_size=24).next_to(end_dot, DOWN)
        self.play(FadeIn(end_dot), Write(end_label))
        self.wait(2)