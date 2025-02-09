import pyvista as pv
axes = pv.Axes()
axes.axes_actor.x_label = 'This axis'
axes.axes_actor.x_label
# Expected:
## 'This axis'
