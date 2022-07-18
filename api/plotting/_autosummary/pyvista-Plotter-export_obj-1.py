# Export the scene to "scene.obj"
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.export_obj('scene.obj')  # doctest:+SKIP
