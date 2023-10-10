# Merge three separate spheres into a single mesh.
#
import pyvista as pv
sphere_a = pv.Sphere(center=(1, 0, 0))
sphere_b = pv.Sphere(center=(0, 1, 0))
sphere_c = pv.Sphere(center=(0, 0, 1))
merged = sphere_a.merge([sphere_b, sphere_c])
merged.plot()
