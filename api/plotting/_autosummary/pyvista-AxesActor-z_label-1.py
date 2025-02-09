import pyvista as pv
axes = pv.Axes()
axes.axes_actor.z_label = 'This axis'
axes.axes_actor.z_label
# Expected:
## 'This axis'
