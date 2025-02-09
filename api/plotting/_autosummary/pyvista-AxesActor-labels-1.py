import pyvista as pv
axes_actor = pv.AxesActor()
axes_actor.labels = ['X Axis', 'Y Axis', 'Z Axis']
axes_actor.labels
# Expected:
## ('X Axis', 'Y Axis', 'Z Axis')
