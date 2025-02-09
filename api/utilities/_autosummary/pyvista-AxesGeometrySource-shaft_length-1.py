import pyvista as pv
axes_geometry_source = pv.AxesGeometrySource()
axes_geometry_source.shaft_length
# Expected:
## (0.8, 0.8, 0.8)
axes_geometry_source.shaft_length = 0.7
axes_geometry_source.shaft_length
# Expected:
## (0.7, 0.7, 0.7)
axes_geometry_source.shaft_length = (1.0, 0.9, 0.5)
axes_geometry_source.shaft_length
# Expected:
## (1.0, 0.9, 0.5)
