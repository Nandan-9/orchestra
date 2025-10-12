from manim import *

class FourierSeries(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE},
            tips=False
        )
        
        # Add x-axis labels
        labels = VGroup()
        x_points = [PI / 2, PI, 3 * PI / 2, 2 * PI]
        label_texts = ["\\frac{\\pi}{2}", "\\pi", "\\frac{3\\pi}{2}", "2\\pi"]
        
        for x_val, text in zip(x_points, label_texts):
            label = MathTex(text, font_size=24).next_to(axes.c2p(x_val, 0), DOWN, buff=0.1)
            labels.add(label)
        
        # Create sine wave
        sine_wave = axes.plot(lambda x: np.sin(x), x_range=[0, 2 * PI], color=YELLOW)
        
        # Create tracking dot
        dot = Dot(color=RED, radius=0.08)
        
        # Create end marker
        end_dot = Dot(axes.c2p(2 * PI, 0), color=GREEN, radius=0.08)
        end_label = MathTex("(2\\pi, 0)", font_size=24).next_to(end_dot, UP, buff=0.1)
        
        # Animation sequence
        self.play(Create(axes), run_time=1)
        self.play(Write(labels), run_time=1)
        self.wait(0.5)
        
        # Animate sine wave with tracking dot
        self.play(
            Create(sine_wave, run_time=4, rate_func=linear),
            MoveAlongPath(dot, sine_wave, run_time=4, rate_func=linear)
        )
        
        # Add end marker
        self.play(FadeIn(end_dot), Write(end_label))
        self.wait(1)