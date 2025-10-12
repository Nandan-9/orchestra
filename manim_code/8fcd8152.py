import numpy as np
from manim import *

class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2*np.pi, np.pi/2],
            y_range=[-1, 1, 0.5],
            axis_config={"color": WHITE},
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": True}
        )
        
        x_labels = VGroup()
        positions = [np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
        texs = [r'\pi/2', r'\pi', r'3\pi/2', r'2\pi']
        for pos, tex in zip(positions, texs):
            label = MathTex(tex, font_size=24).next_to(axes.c2p(pos, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        sine_graph = axes.plot(lambda x: np.sin(x), x_range=[0, 2*np.pi], color=BLUE)
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        
        self.add(axes, x_labels)
        self.play(
            Create(sine_graph, run_time=5, rate_func=linear),
            MoveAlongPath(dot, sine_graph, run_time=5, rate_func=linear)
        )
        
        self.remove(dot)
        end_dot = Dot(color=GREEN).move_to(axes.c2p(2*np.pi, 0))
        end_label = MathTex(r'(2\pi, 0)', font_size=24).next_to(end_dot, DOWN, buff=0.2)
        self.play(Create(end_dot), Write(end_label))
        self.wait(1)