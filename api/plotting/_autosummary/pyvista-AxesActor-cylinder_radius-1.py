import pyvista as pv
axes = pv.Axes()
axes.axes_actor.cylinder_radius
# Expected:
## 0.05
axes.axes_actor.cylinder_radius = 0.03
axes.axes_actor.cylinder_radius
# Expected:
## 0.03
