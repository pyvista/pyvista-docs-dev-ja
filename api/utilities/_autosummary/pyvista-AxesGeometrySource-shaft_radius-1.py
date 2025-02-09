import pyvista as pv
axes_geometry_source = pv.AxesGeometrySource()
axes_geometry_source.shaft_radius
# Expected:
## 0.025
axes_geometry_source.shaft_radius = 0.05
axes_geometry_source.shaft_radius
# Expected:
## 0.05
