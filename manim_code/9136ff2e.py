from manim import *

class SineWave(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 2 * PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": [PI/2, PI, 3*PI/2, 2*PI],
                           "numbers_with_elongated_ticks": [PI/2, PI, 3*PI/2, 2*PI],
                           "decimal_number_config": {"num_decimal_places": 0}},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Add π symbols to x-axis
        x_labels = VGroup(
            MathTex("\\pi/2").next_to(axes.c2p(PI/2, 0), DOWN),
            MathTex("\\pi").next_to(axes.c2p(PI, 0), DOWN),
            MathTex("3\\pi/2").next_to(axes.c2p(3*PI/2, 0), DOWN),
            MathTex("2\\pi").next_to(axes.c2p(2*PI, 0), DOWN)
        )
        
        # Create sine curve
        sine_func = axes.plot(lambda x: np.sin(x), color=YELLOW)
        
        # Create tracking dot
        dot = Dot(color=RED).move_to(axes.c2p(0, 0))
        
        # Create end marker
        end_dot = Dot(axes.c2p(2*PI, 0), color=GREEN)
        end_label = MathTex("(2\\pi, 0)", font_size=24).next_to(end_dot, UR, buff=0.1)
        
        # Animation sequence
        self.play(Create(axes), Write(axes_labels))
        self.play(Write(x_labels))
        
        # Animate sine wave drawing with moving dot
        self.play(
            Create(sine_func),
            UpdateFromFunc(dot, lambda d: d.move_to(sine_func.get_end())),
            rate_func=linear,
            run_time=5
        )
        
        # Add end marker
        self.play(FadeIn(end_dot), Write(end_label))
        self.wait(1)