# Generate default orthogonal planes.
#
import pyvista as pv
from pyvista import examples
planes_source = pv.OrthogonalPlanesSource()
output = planes_source.output
output.plot()
#
# Modify the planes to fit a mesh's bounds.
#
human = examples.download_human()
planes_source.bounds = human.bounds
planes_source.update()
#
# Plot the mesh and the planes.
#
pl = pv.Plotter()
_ = pl.add_mesh(human, scalars='Color', rgb=True)
_ = pl.add_mesh(output, opacity=0.3, show_edges=True)
pl.show()
#
# The planes are centered geometrically, but the frontal plane is positioned a bit
# too far forward. Use :meth:`push` to move the frontal plane.
#
planes_source.push(0.0, -10.0, 0)
planes_source.update()
#
pl = pv.Plotter()
_ = pl.add_mesh(human, scalars='Color', rgb=True)
_ = pl.add_mesh(output, opacity=0.3, show_edges=True, line_width=10)
pl.view_yz()
pl.show()
