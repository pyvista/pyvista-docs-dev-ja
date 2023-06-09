import pyvista as pv
axes = pv.Axes()
axes.axes_actor.shaft_length
# Expected:
## (0.8, 0.8, 0.8)
axes.axes_actor.shaft_length = 0.7
axes.axes_actor.shaft_length
# Expected:
## (0.7, 0.7, 0.7)
axes.axes_actor.shaft_length = (1.0, 0.9, 0.5)
axes.axes_actor.shaft_length
# Expected:
## (1.0, 0.9, 0.5)
