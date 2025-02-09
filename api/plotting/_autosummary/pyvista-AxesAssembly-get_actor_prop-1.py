# Get the ambient property of the axes shafts and tips.
#
import pyvista as pv
axes_assembly = pv.AxesAssembly()
axes_assembly.get_actor_prop('ambient')
# Expected:
## _AxesPropTuple(x_shaft=0.0, y_shaft=0.0, z_shaft=0.0, x_tip=0.0, y_tip=0.0, z_tip=0.0)
