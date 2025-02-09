# Get the default opacity and visualize it.
#
import pyvista as pv
prop = pv.Property()
prop.opacity
# Expected:
## 1.0
#
prop.plot()
#
# Visualize an opacity value of ``0.75``.
#
prop.opacity = 0.75
prop.plot()
#
# Visualize an opacity of ``0.25``.
#
prop.opacity = 0.25
prop.plot()
