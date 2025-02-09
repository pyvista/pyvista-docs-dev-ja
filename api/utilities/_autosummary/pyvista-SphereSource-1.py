# Create a sphere using default parameters.
#
import pyvista as pv
sphere = pv.SphereSource()
sphere.output.plot(show_edges=True)
#
# Create a quarter sphere by setting ``end_theta``.
#
sphere = pv.SphereSource(end_theta=90)
out = sphere.output.plot(show_edges=True)
#
# Create a hemisphere by setting ``end_phi``.
#
sphere = pv.SphereSource(end_phi=90)
out = sphere.output.plot(show_edges=True)
