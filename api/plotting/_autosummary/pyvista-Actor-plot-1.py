# Create an actor without the :class:`pyvista.Plotter`, change its
# properties, and plot it.
#
import pyvista as pv
mesh = pv.Sphere()
mapper = pv.DataSetMapper(mesh)
actor = pv.Actor(mapper=mapper)
actor.prop.color = 'red'
actor.prop.show_edges = True
actor.plot()
