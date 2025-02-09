# Position the labels at the center (along the edges) and plot the assembly.
#
import pyvista as pv
planes = pv.PlanesAssembly(label_position=0)
planes.label_position
# Expected:
## (0.0, 0.0, 0.0)
#
pl = pv.Plotter()
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
#
# Position the labels at the corners.
#
planes.label_position = 1.0
pl = pv.Plotter()
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
#
# Vary the position of the labels independently for each plane. The values may be
# negative and/or exceed a value of ``1.0``.
#
planes.label_position = (-1.3, -1.0, -0.5)
pl = pv.Plotter()
_ = pl.add_actor(planes)
planes.camera = pl.camera
pl.show()
