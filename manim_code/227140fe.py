from manim import *

class SineWave(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 2.5*PI, PI/2],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": BLUE}
        )
        
        # Add labels for key x-values
        labels = VGroup()
        x_points = [PI/2, PI, 3*PI/2, 2*PI]
        for x in x_points:
            label = MathTex(
                f"{int(x/PI)}\\pi" if x != 2*PI else "2\\pi",
                font_size=24
            ).next_to(axes.c2p(x, 0), DOWN)
            labels.add(label)
        
        # Create sine curve
        sine_curve = axes.plot(
            lambda x: np.sin(x),
            x_range=[0, 2*PI],
            color=YELLOW
        )
        
        # Create tracking dot
        dot = Dot(color=RED)
        
        # Create end marker
        end_dot = Dot(axes.c2p(2*PI, 0), color=GREEN)
        end_label = MathTex("(2\\pi, 0)", font_size=24).next_to(end_dot, DOWN)
        
        # Animation sequence
        self.play(Create(axes))
        self.play(Create(labels))
        self.wait(0.5)
        
        # Animate curve drawing with dot tracking
        self.play(
            Create(sine_curve),
            dot.animate.move_to(axes.c2p(0, 0)),
            run_time=3,
            rate_func=linear
        )
        self.add(Updater(dot, lambda d: d.move_to(sine_curve.get_end())))
        
        # Add end marker
        self.play(Create(end_dot), Write(end_label))
        self.wait(1)