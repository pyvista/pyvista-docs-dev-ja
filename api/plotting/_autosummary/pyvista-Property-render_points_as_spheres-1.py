# Get the default point rendering and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.render_points_as_spheres
# Expected:
## False
prop.style = 'points'
prop.point_size = 20
prop.plot()
#
# Visualize rendering points as spheres.
#
prop.render_points_as_spheres = True
prop.plot()
