# Modify the properties of an actor after adding a dataset to the plotter.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
prop = actor.prop
prop.diffuse = 0.6
pl.show()
