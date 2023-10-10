# Create a line between ``(0, 0, 0)`` and ``(0, 0, 1)``.
#
import pyvista as pv
mesh = pv.Line((0, 0, 0), (0, 0, 1))
mesh.plot(color='k', line_width=10)
