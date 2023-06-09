# Create an Axes object and then access the
# visibility attribute of its AxesActor.
#
import pyvista as pv
axes = pv.Axes()
axes.axes_actor.visibility
# Expected:
## True
