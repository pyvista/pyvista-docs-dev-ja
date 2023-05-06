# Enable rendering points as spheres.
#
import pyvista as pv
prop = pv.Property()
prop.style = 'points'
prop.point_size = 20
prop.render_points_as_spheres = True
prop.render_points_as_spheres
# Expected:
## True
#
# Visualize default point rendering.
#
prop.render_points_as_spheres = False
prop.plot()
#
# Visualize rendering points as spheres.
#
prop.render_points_as_spheres = True
prop.plot()
