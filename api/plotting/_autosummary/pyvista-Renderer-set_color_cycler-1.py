# Set the default color cycler to iterate through red, green, and blue.
#
import pyvista as pv
pl = pv.Plotter()
pl.renderer.set_color_cycler(['red', 'green', 'blue'])
_ = pl.add_mesh(pv.Cone(center=(0, 0, 0)))  # red
_ = pl.add_mesh(pv.Cube(center=(1, 0, 0)))  # green
_ = pl.add_mesh(pv.Sphere(center=(1, 1, 0)))  # blue
_ = pl.add_mesh(pv.Cylinder(center=(0, 1, 0)))  # red again
pl.show()
#
# Load a mesh with active scalars and split it into two separate meshes.
#
mesh = pv.Wavelet()
mesh.active_scalars_name
# Expected:
## 'RTData'
#
a = mesh.clip(invert=True)
b = mesh.clip(invert=False)
#
# Enable color cycling and set ``color=True`` to force the meshes to be colored with the
# cycler's colors.
#
pv.global_theme.color_cycler = 'default'
pl = pv.Plotter()
_ = pl.add_mesh(a, color=True)
_ = pl.add_mesh(b, color=True)
pl.show()
