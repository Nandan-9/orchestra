from manim import *
import numpy as np

# Example: 2D Vector Field
class VectorFieldScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
        )

        # Define vector field function: F(x, y) = (-y, x)
        def vector_field(pos):
            x, y = pos[:2]
            return np.array([-y, x, 0])

        # Create the vector field
        field = ArrowVectorField(
            vector_field,
            x_range=[-3, 3, 0.5],
            y_range=[-3, 3, 0.5],
            colors=[BLUE, GREEN],
        )

        # Animate axes and vector field
        self.play(Create(axes))
        self.play(Create(field))
        self.wait(3)
