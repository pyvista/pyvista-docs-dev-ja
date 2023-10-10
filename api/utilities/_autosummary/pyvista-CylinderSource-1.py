# Create a default CylinderSource.
#
import pyvista as pv
source = pv.CylinderSource()
source.output.plot(show_edges=True, line_width=5)
#
# Display a 3D plot of a default :class:`CylinderSource`.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.CylinderSource(), show_edges=True, line_width=5)
pl.show()
#
# Visualize the output of :class:`CylinderSource` in a 3D plot.
#
pl = pv.Plotter()
_ = pl.add_mesh(
    pv.CylinderSource().output, show_edges=True, line_width=5
)
pl.show()
