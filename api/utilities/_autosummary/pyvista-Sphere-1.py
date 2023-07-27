# Create a sphere using default parameters.
#
import pyvista
sphere = pyvista.Sphere()
sphere.plot(show_edges=True)
#
# Create a quarter sphere by setting ``end_theta``.
#
sphere = pyvista.Sphere(end_theta=90)
out = sphere.plot(show_edges=True)
#
# Create a hemisphere by setting ``end_phi``.
#
sphere = pyvista.Sphere(end_phi=90)
out = sphere.plot(show_edges=True)
