# Add a cube to a plot and enable cell picking.
#
import pyvista as pv
cube = pv.Cube()
pl = pv.Plotter()
_ = pl.add_mesh(cube)
_ = pl.enable_surface_point_picking()
