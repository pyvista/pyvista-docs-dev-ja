import pyvista as pv
axes_geometry_source = pv.AxesGeometrySource()
axes_geometry_source.tip_radius
# Expected:
## 0.1
axes_geometry_source.tip_radius = 0.2
axes_geometry_source.tip_radius
# Expected:
## 0.2
