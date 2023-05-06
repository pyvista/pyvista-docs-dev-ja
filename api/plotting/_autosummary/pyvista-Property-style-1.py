# Set the representation style to ``'Wireframe'``
#
import pyvista as pv
prop = pv.Property()
prop.style = 'wireframe'
prop.style
# Expected:
## 'Wireframe'
#
# Visualize default surface representation style.
#
prop.style = 'surface'
prop.plot()
#
# Visualize wireframe representation style.
#
prop.style = 'wireframe'
prop.plot()
#
# Visualize points representation style.
#
prop.style = 'points'
prop.point_size = 5.0
prop.plot()
