# Add a cube to a plot and enable cell picking. Enable ``left_clicking``
# to immediately start picking on the left click and disable showing the
# box. You can still press the ``p`` key to select meshes.
#
import pyvista as pv
cube = pv.Cube()
pl = pv.Plotter()
_ = pl.add_mesh(cube)
_ = pl.enable_surface_picking(left_clicking=True)
