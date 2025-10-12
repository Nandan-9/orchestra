from manim import *

class CosineWave(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": [PI / 2, PI, 3 * PI / 2, 2 * PI]}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Add key points on x-axis
        key_points = [PI / 2, PI, 3 * PI / 2, 2 * PI]
        labels = [
            MathTex(r"\frac{\pi}{2}").next_to(axes.c2p(k, 0), DOWN)
            for k in key_points
        ]
        
        # Create cosine function
        cos_func = axes.plot(np.cos, color=YELLOW, x_range=[0, 2 * PI])
        
        # Create tracker dot
        tracker_dot = Dot(color=RED).move_to(axes.c2p(0, 1))
        
        # Create end point
        end_point = Dot(axes.c2p(2 * PI, 1), color=GREEN)
        end_label = MathTex(r"(2\pi, 1)", font_size=24).next_to(end_point, UR, buff=0.1)
        
        # Animation sequence
        self.play(Create(axes), Write(axes_labels))
        self.play(*[Write(label) for label in labels])
        
        # Animate curve drawing with moving dot
        self.add(tracker_dot)
        self.play(
            Create(cos_func, run_time=4, rate_func=linear),
            UpdateFromFunc(tracker_dot, lambda d: d.move_to(cos_func.get_end())),
        )
        
        # Add end point and label
        self.play(FadeIn(end_point), Write(end_label))
        self.wait()