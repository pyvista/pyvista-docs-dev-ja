# Set opacity to ``0.5``.
#
import pyvista as pv
prop = pv.Property()
prop.opacity = 0.5
prop.opacity
# Expected:
## 0.5
#
# Visualize default opacity of ``1.0``.
#
prop.opacity = 1.0
prop.plot()
#
# Visualize opacity of ``0.75``.
#
prop.opacity = 0.75
prop.plot()
#
# Visualize opacity of ``0.25``.
#
prop.opacity = 0.25
prop.plot()
