# Show axes without labels and with thick lines.
#
import pyvista
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Box(), show_edges=True)
_ = pl.add_axes(line_width=5, labels_off=True)
pl.show()
#
# Use the axes orientation widget instead of the default arrows.
#
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Sphere())
_ = pl.add_axes(box=True)
pl.show()
#
# Specify more parameters for the axes marker.
#
import pyvista
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Box(), show_edges=True)
_ = pl.add_axes(
    line_width=5,
    cone_radius=0.6,
    shaft_length=0.7,
    tip_length=0.3,
    ambient=0.5,
    label_size=(0.4, 0.16),
)
pl.show()
