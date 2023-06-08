import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).bounds
# Expected:
## (-0.05405950918793678, -5.551115123125783e-17, 0.0, 0.011239604093134403, -0.5, -0.49706897139549255)
