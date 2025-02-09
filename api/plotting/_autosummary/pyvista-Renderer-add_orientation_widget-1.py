# Use an Arrow as the orientation widget.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Cube(), show_edges=True)
widget = pl.add_orientation_widget(pv.Arrow(), color='r')
pl.show()
