from manim import *


class MinimalScene(Scene):
    def construct(self):
        # Create a simple text object
        text = Text("Hello, Manim!", font_size=72)

        # Animate writing the text on screen
        self.play(Write(text))

        # Keep it visible for a while
        self.wait(2)
