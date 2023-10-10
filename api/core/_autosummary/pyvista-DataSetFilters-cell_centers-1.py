import pyvista as pv
mesh = pv.Plane()
mesh.point_data.clear()
centers = mesh.cell_centers()
pl = pv.Plotter()
actor = pl.add_mesh(mesh, show_edges=True)
actor = pl.add_points(
    centers,
    render_points_as_spheres=True,
    color='red',
    point_size=20,
)
pl.show()
