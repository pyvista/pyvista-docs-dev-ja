import pyvista as pv
sphere_a = pv.Sphere()
sphere_b = pv.Sphere(center=(0.5, 0, 0))
merged = sphere_a.merge(sphere_b)
merged.plot(style='wireframe', color='lightblue')
