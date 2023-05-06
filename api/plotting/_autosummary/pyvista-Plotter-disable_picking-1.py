# Enable and then disable picking.
#
import pyvista as pv
mesh = pv.Sphere(center=(1, 0, 0))
cube = pv.Cube()
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
_ = pl.add_mesh(cube)
_ = pl.enable_mesh_picking(left_clicking=True)
pl.disable_picking()
