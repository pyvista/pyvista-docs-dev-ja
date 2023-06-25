# Add a sphere and a cube to a plot and enable mesh picking. Enable
# ``left_clicking`` to immediately start picking on the left click and
# disable showing the box. You can still press the ``p`` key to select
# meshes.
#
import pyvista as pv
mesh = pv.Sphere(center=(1, 0, 0))
cube = pv.Cube()
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
_ = pl.add_mesh(cube)
_ = pl.enable_mesh_picking()
