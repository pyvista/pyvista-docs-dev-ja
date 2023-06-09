import pyvista as pv
axes = pv.Axes()
axes.axes_actor.sphere_radius
# Expected:
## 0.4
axes.axes_actor.sphere_radius = 0.8
axes.axes_actor.sphere_radius
# Expected:
## 0.8
