# Probe the active scalars in ``grid`` at the points in ``mesh``.
#
import pyvista as pv
from pyvista import examples
mesh = pv.Sphere(center=(4.5, 4.5, 4.5), radius=4.5)
grid = examples.load_uniform()
result = grid.probe(mesh)  # doctest:+SKIP
'Spatial Point Data' in result.point_data  # doctest:+SKIP
# Expected:
## True
