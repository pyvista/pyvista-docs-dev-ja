import pyvista as pv
axes = pv.Axes()
axes.axes_actor.y_label = 'This axis'
axes.axes_actor.y_label
# Expected:
## 'This axis'
