# Add symmetric axes to a plot.
#
import pyvista as pv
axes_assembly = pv.AxesAssemblySymmetric()
pl = pv.Plotter()
_ = pl.add_actor(axes_assembly)
pl.show()
#
# Customize the axes labels.
#
axes_assembly.labels = [
    'east',
    'west',
    'north',
    'south',
    'up',
    'down',
]
axes_assembly.label_color = 'darkgoldenrod'
#
pl = pv.Plotter()
_ = pl.add_actor(axes_assembly)
pl.show()
#
# Add the axes as a custom orientation widget with
# :func:`~pyvista.Renderer.add_orientation_widget`. We also configure the labels to
# only show text for the positive axes.
#
axes_assembly = pv.AxesAssemblySymmetric(
    x_label=('X', ''), y_label=('Y', ''), z_label=('Z', '')
)
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cone())
_ = pl.add_orientation_widget(
    axes_assembly,
    viewport=(0, 0, 0.5, 0.5),
)
pl.show()
