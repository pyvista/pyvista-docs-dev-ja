# Demonstrate a boolean intersection with two spheres.  Note how
# the final mesh only includes the intersection of the two.
#
import pyvista as pv
sphere_a = pv.Sphere()
sphere_b = pv.Sphere(center=(0.5, 0, 0))
result = sphere_a & sphere_b
pl = pv.Plotter()
_ = pl.add_mesh(sphere_a, color='r', style='wireframe', line_width=3)
_ = pl.add_mesh(sphere_b, color='b', style='wireframe', line_width=3)
_ = pl.add_mesh(result, color='lightblue')
pl.camera_position = 'xz'
pl.show()
