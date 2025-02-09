# Customize the axis shaft color and shape.
#
import pyvista as pv
#
axes = pv.Axes()
axes.axes_actor.z_axis_shaft_properties.color = (0.0, 1.0, 1.0)
axes.axes_actor.shaft_type = axes.axes_actor.ShaftType.CYLINDER
pl = pv.Plotter()
_ = pl.add_actor(axes.axes_actor)
_ = pl.add_mesh(pv.Sphere())
pl.show()
#
# Or you can use this as a custom orientation widget with
# :func:`add_orientation_widget() <pyvista.Renderer.add_orientation_widget>`:
#
import pyvista as pv
#
axes = pv.Axes()
axes_actor = axes.axes_actor
axes.axes_actor.shaft_type = 0
#
axes_actor.x_axis_shaft_properties.color = (1.0, 1.0, 1.0)
axes_actor.y_axis_shaft_properties.color = (1.0, 1.0, 1.0)
axes_actor.z_axis_shaft_properties.color = (1.0, 1.0, 1.0)
#
axes_actor.x_label = 'U'
axes_actor.y_label = 'V'
axes_actor.z_label = 'W'
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cone())
_ = pl.add_orientation_widget(
    axes_actor,
    viewport=(0, 0, 0.5, 0.5),
)
pl.show()
