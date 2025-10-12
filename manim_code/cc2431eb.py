from manim import *

class SineWave(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": [0, PI/2, PI, 3*PI/2, 2*PI]}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Add key points on x-axis
        key_points = [PI/2, PI, 3*PI/2, 2*PI]
        labels = VGroup()
        for x_val in key_points:
            point = axes.c2p(x_val, 0)
            label = MathTex(
                f"{x_val/PI:.1f}\\pi" if x_val != 2*PI else "2\\pi",
                font_size=24
            ).next_to(point, DOWN)
            labels.add(label)
        
        # Create sine wave
        sine_wave = axes.plot(lambda x: np.sin(x), x_range=[0, 2*PI], color=YELLOW)
        
        # Create tracking dot
        dot = Dot(color=RED, radius=0.08)
        dot.move_to(axes.c2p(0, 0))
        
        # Create end marker
        end_point = axes.c2p(2*PI, 0)
        end_dot = Dot(end_point, color=GREEN, radius=0.08)
        end_label = MathTex("(2\\pi, 0)", font_size=24).next_to(end_dot, UP)
        
        # Animation sequence
        self.play(Create(axes), Write(axes_labels))
        self.play(Write(labels))
        
        # Animate sine wave with tracking dot
        self.play(
            Create(sine_wave),
            UpdateFromFunc(dot, lambda d: d.move_to(sine_wave.get_end())),
            run_time=5,
            rate_func=linear
        )
        
        # Add end marker
        self.play(Create(end_dot), Write(end_label))
        self.wait(1)