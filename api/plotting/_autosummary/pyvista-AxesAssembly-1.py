# Add axes to a plot.
#
import pyvista as pv
axes = pv.AxesAssembly()
pl = pv.Plotter()
_ = pl.add_actor(axes)
pl.show()
#
# Customize the axes colors. Set each axis to a single color, or set the colors of
# each shaft and tip separately with two colors.
#
axes.x_color = ['cyan', 'blue']
axes.y_color = ['magenta', 'red']
axes.z_color = 'yellow'
#
# Customize the label color too.
#
axes.label_color = 'brown'
#
pl = pv.Plotter()
_ = pl.add_actor(axes)
pl.show()
#
# Create axes with custom geometry. Use pyramid shafts and hemisphere tips and
# modify the lengths.
#
axes = pv.AxesAssembly(
    shaft_type='pyramid',
    tip_type='hemisphere',
    tip_length=0.1,
    shaft_length=(0.5, 1.0, 1.5),
)
pl = pv.Plotter()
_ = pl.add_actor(axes)
pl.show()
#
# Position and orient the axes in space.
#
axes = pv.AxesAssembly(position=(1.0, 2.0, 3.0), orientation=(10, 20, 30))
pl = pv.Plotter()
_ = pl.add_actor(axes)
pl.show()
#
# Add the axes as a custom orientation widget with
# :func:`~pyvista.Renderer.add_orientation_widget`:
#
import pyvista as pv
#
axes = pv.AxesAssembly(symmetric_bounds=True)
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cone())
_ = pl.add_orientation_widget(
    axes,
    viewport=(0, 0, 0.5, 0.5),
)
pl.show()
