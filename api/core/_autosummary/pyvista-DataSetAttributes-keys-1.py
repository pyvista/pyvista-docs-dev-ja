import pyvista as pv
mesh = pv.Sphere()
mesh.clear_data()
mesh.point_data['data0'] = [0] * mesh.n_points
mesh.point_data['data1'] = range(mesh.n_points)
mesh.point_data.keys()
# Expected:
## ['data0', 'data1']
