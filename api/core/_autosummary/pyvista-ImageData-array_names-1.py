# Return the array names for a mesh.
#
import pyvista as pv
mesh = pv.Sphere()
mesh.point_data['my_array'] = range(mesh.n_points)
mesh.array_names
# Expected:
## ['my_array', 'Normals']
