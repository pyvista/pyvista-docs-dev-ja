# Show a list of all shaft type options.
#
import pyvista as pv
pv.AxesGeometrySource.GEOMETRY_TYPES
# Expected:
## ('cylinder', 'sphere', 'hemisphere', 'cone', 'pyramid', 'cube', 'octahedron')
#
# Show the default shaft type and modify it.
#
axes_geometry_source = pv.AxesGeometrySource()
axes_geometry_source.shaft_type
# Expected:
## 'cylinder'
axes_geometry_source.shaft_type = 'cube'
axes_geometry_source.shaft_type
# Expected:
## 'cube'
#
# Set the shaft type to any 3-dimensional dataset.
#
axes_geometry_source.shaft_type = pv.Superquadric()
axes_geometry_source.shaft_type
# Expected:
## 'custom'
