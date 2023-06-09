import pyvista as pv
axes = pv.Axes()
axes.axes_actor.cylinder_resolution
# Expected:
## 16
axes.axes_actor.cylinder_resolution = 24
axes.axes_actor.cylinder_resolution
# Expected:
## 24
