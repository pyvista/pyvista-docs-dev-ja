import pyvista as pv
axes = pv.Axes()
axes.axes_actor.tip_type = axes.axes_actor.TipType.SPHERE
axes.axes_actor.tip_type
# Expected:
## <TipType.SPHERE: 1>
