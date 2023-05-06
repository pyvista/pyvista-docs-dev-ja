# Create a mapper outside :class:`pyvista.Plotter` and assign it to an
# actor.
#
import pyvista as pv
mesh = pv.Cube()
mapper = pv.DataSetMapper(dataset=mesh)
actor = pv.Actor(mapper=mapper)
actor.plot()
