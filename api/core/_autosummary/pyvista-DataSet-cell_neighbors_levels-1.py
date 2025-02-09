# Get the cell neighbors IDs starting from the 0-th cell
# up until the third level.
#
import pyvista as pv
mesh = pv.Sphere(theta_resolution=10)
nbr_levels = mesh.cell_neighbors_levels(0, connections='edges', n_levels=3)
nbr_levels = list(nbr_levels)
nbr_levels[0]
# Expected:
## [1, 21, 9]
nbr_levels[1]
# Expected:
## [2, 8, 74, 75, 20, 507]
nbr_levels[2]
# Expected:
## [128, 129, 3, 453, 7, 77, 23, 506]
#
# Visualize these cells IDs.
#
from functools import partial
pv.global_theme.color_cycler = [
    'red',
    'green',
    'blue',
    'purple',
]
pl = pv.Plotter()
add_point_labels = partial(
    pl.add_point_labels,
    text_color='white',
    font_size=40,
    shape=None,
    show_points=False,
)
cell = mesh.extract_cells(0)
_ = pl.add_mesh(cell, show_edges=True)
_ = add_point_labels(cell.cell_centers().points, labels=['0'])
other_ids = [0]
neighbors = mesh.cell_neighbors_levels(0, connections='edges', n_levels=3)
for i, ids in enumerate(neighbors, start=1):
    cells = mesh.extract_cells(ids)
    _ = pl.add_mesh(cells, show_edges=True)
    _ = add_point_labels(
        cells.cell_centers().points, labels=[f'{i}'] * len(ids)
    )
    other_ids.extend(ids)
cells = mesh.extract_cells(other_ids, invert=True)
_ = pl.add_mesh(cells, color='white', show_edges=True)
pl.view_xy()
pl.camera.zoom(6.0)
pl.show()
