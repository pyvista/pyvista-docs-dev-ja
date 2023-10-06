# Create a default CylinderSource.
#
import pyvista
source = pyvista.CylinderSource()
source.output.plot(show_edges=True, line_width=5)
#
# Display a 3D plot of a default :class:`CylinderSource`.
#
import pyvista
pl = pyvista.Plotter()
_ = pl.add_mesh(
    pyvista.CylinderSource(), show_edges=True, line_width=5
)
pl.show()
#
# Visualize the output of :class:`CylinderSource` in a 3D plot.
#
pl = pyvista.Plotter()
_ = pl.add_mesh(
    pyvista.CylinderSource().output, show_edges=True, line_width=5
)
pl.show()
