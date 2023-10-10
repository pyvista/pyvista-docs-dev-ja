# Create a tube between ``(0, 0, 0)`` and ``(0, 0, 1)``.
#
import pyvista as pv
mesh = pv.Tube((0, 0, 0), (0, 0, 1))
mesh.plot()
