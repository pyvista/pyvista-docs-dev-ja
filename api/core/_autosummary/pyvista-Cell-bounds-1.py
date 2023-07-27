import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).bounds
# Expected:
## (0.0, 0.05405950918793678, 0.0, 0.011239604093134403, 0.49706897139549255, 0.5)
