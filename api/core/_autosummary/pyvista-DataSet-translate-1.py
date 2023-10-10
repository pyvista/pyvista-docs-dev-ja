# Create a sphere and translate it by ``(2, 1, 2)``.
#
import pyvista as pv
mesh = pv.Sphere()
mesh.center
# Expected:
## [0.0, 0.0, 0.0]
trans = mesh.translate((2, 1, 2), inplace=False)
trans.center
# Expected:
## [2.0, 1.0, 2.0]
