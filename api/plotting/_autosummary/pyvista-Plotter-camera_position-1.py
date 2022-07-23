# Return camera's position and then reposition it via a list of tuples.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_bunny_coarse()
pl = pv.Plotter()
_ = pl.add_mesh(mesh, show_edges=True, reset_camera=True)
pl.camera_position
# Expected:
## [(0.02430, 0.0336, 0.9446),
##  (0.02430, 0.0336, -0.02225),
##  (0.0, 1.0, 0.0)]
pl.camera_position = [
    (0.3914, 0.4542, 0.7670),
    (0.0243, 0.0336, -0.0222),
    (-0.2148, 0.8998, -0.3796),
]
pl.show()
#
# Set the camera position using a string and look at the ``'xy'`` plane.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, show_edges=True)
pl.camera_position = 'xy'
pl.show()
#
# Set the camera position using a string and look at the ``'zy'`` plane.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, show_edges=True)
pl.camera_position = 'zy'
pl.show()
