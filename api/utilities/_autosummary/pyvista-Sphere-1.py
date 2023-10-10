# Create a sphere using default parameters.
#
import pyvista as pv
sphere = pv.Sphere()
sphere.plot(show_edges=True)
#
# Create a quarter sphere by setting ``end_theta``.
#
sphere = pv.Sphere(end_theta=90)
out = sphere.plot(show_edges=True)
#
# Create a hemisphere by setting ``end_phi``.
#
sphere = pv.Sphere(end_phi=90)
out = sphere.plot(show_edges=True)
