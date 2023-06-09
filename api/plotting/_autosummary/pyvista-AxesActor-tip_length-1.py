import pyvista as pv
axes = pv.Axes()
axes.axes_actor.tip_length
# Expected:
## (0.2, 0.2, 0.2)
axes.axes_actor.tip_length = 0.3
axes.axes_actor.tip_length
# Expected:
## (0.3, 0.3, 0.3)
axes.axes_actor.tip_length = (0.1, 0.4, 0.2)
axes.axes_actor.tip_length
# Expected:
## (0.1, 0.4, 0.2)
