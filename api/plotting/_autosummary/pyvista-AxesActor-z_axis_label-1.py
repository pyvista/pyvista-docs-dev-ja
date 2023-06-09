import pyvista as pv
axes = pv.Axes()
axes.axes_actor.z_axis_label = 'This axis'
axes.axes_actor.z_axis_label
# Expected:
## 'This axis'
