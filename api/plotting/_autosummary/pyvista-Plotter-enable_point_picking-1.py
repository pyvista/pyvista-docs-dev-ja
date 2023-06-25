# Enable point picking with a custom message.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
_ = pl.add_mesh(pv.Cube(), pickable=False)
pl.enable_point_picking(show_message='Pick a point')
