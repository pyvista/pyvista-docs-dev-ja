import pyvista as pv
axes_geometry_source = pv.AxesGeometrySource()
axes_geometry_source.tip_length
# Expected:
## (0.2, 0.2, 0.2)
axes_geometry_source.tip_length = 0.3
axes_geometry_source.tip_length
# Expected:
## (0.3, 0.3, 0.3)
axes_geometry_source.tip_length = (0.1, 0.4, 0.2)
axes_geometry_source.tip_length
# Expected:
## (0.1, 0.4, 0.2)
