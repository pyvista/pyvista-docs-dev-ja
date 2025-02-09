# Get the cell ids using the 0-th point.
#
import pyvista as pv
mesh = pv.Sphere(theta_resolution=10)
mesh.point_cell_ids(0)
# Expected:
## [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Plot them.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, show_edges=True)
_ = pl.add_point_labels(
    mesh.points[0], ['0'], text_color='blue', font_size=20
)
ids = mesh.point_cell_ids(0)
cells = mesh.extract_cells(ids)
_ = pl.add_mesh(cells, color='red', show_edges=True)
centers = cells.cell_centers().points
_ = pl.add_point_labels(
    centers,
    labels=[f'{i}' for i in ids],
    text_color='white',
    font_size=20,
    shape=None,
    show_points=False,
)
others = mesh.extract_cells(
    [i for i in range(mesh.n_cells) if i not in ids]
)
_ = pl.add_mesh(others, show_edges=True)
pl.camera_position = 'xy'
pl.camera.zoom(7.0)
pl.show()
