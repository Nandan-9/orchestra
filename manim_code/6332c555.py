import numpy as np
from manim import *

class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": []}
        )
        
        x_labels = {
            PI/2: MathTex(r"\\frac{\\pi}{2}", font_size=24),
            PI: MathTex(r"\\pi", font_size=24),
            3*PI/2: MathTex(r"\\frac{3\\pi}{2}", font_size=24),
            2*PI: MathTex(r"2\\pi", font_size=24)
        }
        
        for x_val, label in x_labels.items():
            label.next_to(axes.c2p(x_val, 0), DOWN)
            self.add(label)
        
        sine_graph = axes.plot(
            lambda x: np.sin(x),
            x_range=[0, 2*PI],
            color=YELLOW
        )
        
        tracker = ValueTracker(0)
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        
        def dot_updater(d):
            x = tracker.get_value()
            d.move_to(axes.c2p(x, np.sin(x)))
            
        dot.add_updater(dot_updater)
        
        self.play(
            Create(axes),
            run_time=1
        )
        self.add(dot)
        self.play(
            Create(sine_graph),
            tracker.animate.set_value(2*PI),
            run_time=5,
            rate_func=linear
        )
        dot.remove_updater(dot_updater)
        
        end_dot = Dot(axes.c2p(2*PI, 0), color=GREEN)
        end_label = MathTex(r"(2\\pi, 0)", font_size=24).next_to(end_dot, DOWN)
        
        self.play(
            FadeIn(end_dot),
            Write(end_label)
        )
        self.wait(2)