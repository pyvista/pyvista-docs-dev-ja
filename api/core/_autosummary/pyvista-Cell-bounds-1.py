import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).bounds
# Expected:
## BoundsTuple(x_min=0.0, x_max=0.05405950918793678, y_min=0.0, y_max=0.011239604093134403, z_min=0.49706897139549255, z_max=0.5)
