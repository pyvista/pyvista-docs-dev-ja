# Set :attr:`~pyvista.Property.ambient` for all axes shafts and tips to a
# single value.
#
import pyvista as pv
axes_assembly = pv.AxesAssembly()
axes_assembly.set_actor_prop('ambient', 0.7)
axes_assembly.get_actor_prop('ambient')
# Expected:
## _AxesPropTuple(x_shaft=0.7, y_shaft=0.7, z_shaft=0.7, x_tip=0.7, y_tip=0.7, z_tip=0.7)
#
# Set the property again, but this time set separate values for each part.
#
values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
axes_assembly.set_actor_prop('ambient', values)
axes_assembly.get_actor_prop('ambient')
# Expected:
## _AxesPropTuple(x_shaft=0.1, y_shaft=0.2, z_shaft=0.3, x_tip=0.4, y_tip=0.5, z_tip=0.6)
#
# Set :attr:`~pyvista.Property.opacity` for the x-axis only. The property is set
# for both the axis shaft and tip by default.
#
axes_assembly.set_actor_prop('opacity', 0.5, axis='x')
axes_assembly.get_actor_prop('opacity')
# Expected:
## _AxesPropTuple(x_shaft=0.5, y_shaft=1.0, z_shaft=1.0, x_tip=0.5, y_tip=1.0, z_tip=1.0)
#
# Set the property again, but this time set separate values for the shaft and tip.
#
axes_assembly.set_actor_prop('opacity', [0.3, 0.7], axis='x')
axes_assembly.get_actor_prop('opacity')
# Expected:
## _AxesPropTuple(x_shaft=0.3, y_shaft=1.0, z_shaft=1.0, x_tip=0.7, y_tip=1.0, z_tip=1.0)
#
# Set :attr:`~pyvista.Property.show_edges` for the axes shafts only. The property
# is set for all axes by default.
#
axes_assembly.set_actor_prop('show_edges', True, part='shaft')
axes_assembly.get_actor_prop('show_edges')
# Expected:
## _AxesPropTuple(x_shaft=True, y_shaft=True, z_shaft=True, x_tip=False, y_tip=False, z_tip=False)
#
# Set the property again, but this time set separate values for each shaft.
#
axes_assembly.set_actor_prop(
    'show_edges', [True, False, True], part='shaft'
)
axes_assembly.get_actor_prop('show_edges')
# Expected:
## _AxesPropTuple(x_shaft=True, y_shaft=False, z_shaft=True, x_tip=False, y_tip=False, z_tip=False)
#
# Set :attr:`~pyvista.Property.style` for a single axis and specific part.
#
axes_assembly.set_actor_prop('style', 'wireframe', axis='x', part='shaft')
axes_assembly.get_actor_prop('style')
# Expected:
## _AxesPropTuple(x_shaft='Wireframe', y_shaft='Surface', z_shaft='Surface', x_tip='Surface', y_tip='Surface', z_tip='Surface')
