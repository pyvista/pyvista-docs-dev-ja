# Show a list of all shaft type options.
#
import pyvista as pv
pv.AxesGeometrySource.GEOMETRY_TYPES
# Expected:
## ('cylinder', 'sphere', 'hemisphere', 'cone', 'pyramid', 'cube', 'octahedron')
#
# Show the default tip type and modify it.
#
axes_geometry_source = pv.AxesGeometrySource()
axes_geometry_source.tip_type
# Expected:
## 'cone'
axes_geometry_source.tip_type = 'sphere'
axes_geometry_source.tip_type
# Expected:
## 'sphere'
#
# Set the tip type to any 3-dimensional dataset.
#
axes_geometry_source.tip_type = pv.Text3D('O')
axes_geometry_source.tip_type
# Expected:
## 'custom'
#
axes_geometry_source.output.plot(cpos='xy')
