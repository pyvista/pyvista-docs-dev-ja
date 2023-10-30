# Merge two polydata datasets.
#
import pyvista as pv
sphere = pv.Sphere(center=(0, 0, 1))
cube = pv.Cube()
mesh = pv.merge([cube, sphere])
mesh.plot()
