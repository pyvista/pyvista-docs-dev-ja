import pyvista as pv
axes = pv.Axes()
axes.axes_actor.shaft_type = axes.axes_actor.ShaftType.LINE
axes.axes_actor.shaft_type
# Expected:
## <ShaftType.LINE: 1>
