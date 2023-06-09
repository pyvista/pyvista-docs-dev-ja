import pyvista as pv
axes = pv.Axes()
axes.axes_actor.label_position
# Expected:
## (1.0, 1.0, 1.0)
axes.axes_actor.label_position = 0.3
axes.axes_actor.label_position
# Expected:
## (0.3, 0.3, 0.3)
axes.axes_actor.label_position = (0.1, 0.4, 0.2)
axes.axes_actor.label_position
# Expected:
## (0.1, 0.4, 0.2)
