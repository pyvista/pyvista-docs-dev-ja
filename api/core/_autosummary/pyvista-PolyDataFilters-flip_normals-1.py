# Flip the normals of a sphere and plot the normals before and
# after the flip.
#
import pyvista as pv
sphere = pv.Sphere()
sphere.plot_normals(mag=0.1)
sphere.flip_normals()  # doctest:+SKIP
sphere.plot_normals(mag=0.1, opacity=0.5)
