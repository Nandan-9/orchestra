from manim import *

class TransformationsScene(Scene):
    def construct(self):
        # Create shapes
        square = Square(color=BLUE).shift(LEFT*3)
        circle = Circle(color=RED).shift(RIGHT*3)
        triangle = Triangle(color=GREEN)

        # Animate: basic rotations
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))        # Rotate 45 degrees
        self.wait(0.5)
        self.play(square.animate.rotate(-PI/2))       # Rotate -90 degrees
        self.wait(0.5)

        # Animate: scaling
        self.play(Create(circle))
        self.play(circle.animate.scale(1.5))         # Enlarge
        self.wait(0.5)
        self.play(circle.animate.scale(0.5))         # Shrink back
        self.wait(0.5)

        # Animate: shifting / moving
        self.play(Create(triangle))
        self.play(triangle.animate.shift(RIGHT*2))   # Move right
        self.wait(0.5)
        self.play(triangle.animate.shift(UP*2))      # Move up
        self.wait(0.5)
        self.play(triangle.animate.shift(LEFT*3 + DOWN*1))  # Move diagonally
        self.wait(1)

        # Combine transformations
        self.play(
            square.animate.rotate(PI/2).scale(0.8).shift(RIGHT*2),
            circle.animate.rotate(-PI/4).scale(1.2).shift(LEFT*2)
        )
        self.wait(2)
