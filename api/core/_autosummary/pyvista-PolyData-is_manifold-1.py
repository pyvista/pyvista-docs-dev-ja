# Show a sphere is manifold.
#
import pyvista
pyvista.Sphere().is_manifold
# Expected:
## True
#
# Show a plane is not manifold.
#
pyvista.Plane().is_manifold
# Expected:
## False
