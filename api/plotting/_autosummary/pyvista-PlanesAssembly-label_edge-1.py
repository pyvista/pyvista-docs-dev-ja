# Position the labels at the top edge and plot.
#
import pyvista as pv
planes = pv.PlanesAssembly(label_edge='top')
planes.label_edge
# Expected:
## ('top', 'top', 'top')
#
pl = pv.Plotter()
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
#
# Position the labels at the bottom.
#
planes.label_edge = 'bottom'
pl = pv.Plotter()
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
#
# Vary the edge of the labels independently for each plane.
#
planes.label_edge = ('top', 'right', 'left')
pl = pv.Plotter()
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
