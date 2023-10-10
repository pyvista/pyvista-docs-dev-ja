# Create a camera at the pyvista module level.
#
import pyvista as pv
camera = pv.Camera()
#
# Access the active camera of a plotter and get the position of the
# camera.
#
pl = pv.Plotter()
pl.camera.position
# Expected:
## (1.0, 1.0, 1.0)
