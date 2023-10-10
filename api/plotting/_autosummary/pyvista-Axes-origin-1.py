import pyvista as pv
axes = pv.Axes()
axes.origin
# Expected:
## (0.0, 0.0, 0.0)
#
# Set the origin of the camera.
#
axes.origin = (2.0, 1.0, 1.0)
axes.origin
# Expected:
## (2.0, 1.0, 1.0)
