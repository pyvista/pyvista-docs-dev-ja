# Set the default color cycler to iterate through red, green, and blue.
#
import pyvista as pv
pv.global_theme.color_cycler = ['red', 'green', 'blue']
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cone(center=(0, 0, 0)))  # red
_ = pl.add_mesh(pv.Cube(center=(1, 0, 0)))  # green
_ = pl.add_mesh(pv.Sphere(center=(1, 1, 0)))  # blue
_ = pl.add_mesh(pv.Cylinder(center=(0, 1, 0)))  # red again
pl.show()  # doctest: +SKIP
