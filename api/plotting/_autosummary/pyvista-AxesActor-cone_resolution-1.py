import pyvista as pv
axes = pv.Axes()
axes.axes_actor.cone_resolution
# Expected:
## 16
axes.axes_actor.cone_resolution = 24
axes.axes_actor.cone_resolution
# Expected:
## 24
