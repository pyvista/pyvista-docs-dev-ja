import pyvista as pv
axes = pv.Axes()
axes.axes_actor.total_length
# Expected:
## (1.0, 1.0, 1.0)
axes.axes_actor.total_length = 1.2
axes.axes_actor.total_length
# Expected:
## (1.2, 1.2, 1.2)
axes.axes_actor.total_length = (1.0, 0.9, 0.5)
axes.axes_actor.total_length
# Expected:
## (1.0, 0.9, 0.5)
