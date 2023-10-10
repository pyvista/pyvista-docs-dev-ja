# Show a sphere is manifold.
#
import pyvista as pv
pv.Sphere().is_manifold
# Expected:
## True
#
# Show a plane is not manifold.
#
pv.Plane().is_manifold
# Expected:
## False
