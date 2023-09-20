# Create an actor without using :class:`pyvista.Plotter`.
#
import pyvista as pv
mesh = pv.Sphere()
mapper = pv.DataSetMapper(mesh)
actor = pv.Actor(mapper=mapper)
actor
# Expected:
## Actor (...)
##   Center:                     (0.0, 0.0, 0.0)
##   Pickable:                   True
##   Position:                   (0.0, 0.0, 0.0)
##   Scale:                      (1.0, 1.0, 1.0)
##   Visible:                    True
##   X Bounds                    -4.993E-01, 4.993E-01
##   Y Bounds                    -4.965E-01, 4.965E-01
##   Z Bounds                    -5.000E-01, 5.000E-01
##   User matrix:                Set
##   Has mapper:                 True
## ...
#
# Change the actor properties and plot the actor.
#
import pyvista as pv
mesh = pv.Sphere()
mapper = pv.DataSetMapper(mesh)
actor = pv.Actor(mapper=mapper)
actor.prop.color = 'blue'
actor.plot()
#
# Create an actor using the :class:`pyvista.Plotter` and then change the
# visibility of the actor.
#
import pyvista as pv
pl = pv.Plotter()
mesh = pv.Sphere()
actor = pl.add_mesh(mesh)
actor.visibility = False
actor.visibility
# Expected:
## False
