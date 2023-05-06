# Create a multiple lines between ``(0, 0, 0)``, ``(1, 1, 1)`` and ``(0, 0, 1)``.
#
import pyvista
mesh = pyvista.MultipleLines(
    points=[[0, 0, 0], [1, 1, 1], [0, 0, 1]]
)
mesh.plot(color='k', line_width=10)
