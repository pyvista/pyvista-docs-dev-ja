from pyvista import examples
mesh = examples.load_airplane()
#
# Get the neighbor cell ids that have at least one point in common with
# the 0-th cell.
#
mesh.cell_neighbors(0, "points")
# Expected:
## [1, 2, 3, 388, 389, 11, 12, 395, 14, 209, 211, 212]
#
# Get the neighbor cell ids that have at least one edge in common with
# the 0-th cell.
#
mesh.cell_neighbors(0, "edges")
# Expected:
## [1, 3, 12]
#
# For unstructured grids with cells of dimension 3 (Tetrahedron for example),
# cell neighbors can be defined using faces.
#
mesh = examples.download_tetrahedron()
mesh.cell_neighbors(0, "faces")
# Expected:
## [1, 5, 7]
#
# Show a visual example.
#
from functools import partial
import pyvista
mesh = pyvista.Sphere(theta_resolution=10)
pl = pyvista.Plotter(shape=(1, 2))
pl.link_views()
add_point_labels = partial(
    pl.add_point_labels,
    text_color="white",
    font_size=20,
    shape=None,
    show_points=False,
)
for i, connection in enumerate(["points", "edges"]):
    pl.subplot(0, i)
    pl.view_yx()
    _ = pl.add_title(
        f"{connection.capitalize()} neighbors",
        color="red",
        shadow=True,
        font_size=8,
    )

    # Add current cell
    i_cell = 0
    current_cell = mesh.extract_cells(i_cell)
    _ = pl.add_mesh(
        current_cell, show_edges=True, color="blue"
    )
    _ = add_point_labels(
        current_cell.cell_centers().points,
        labels=[f"{i_cell}"],
    )

    # Add neighbors
    ids = mesh.cell_neighbors(i_cell, connection)
    cells = mesh.extract_cells(ids)
    _ = pl.add_mesh(cells, color="red", show_edges=True)
    _ = add_point_labels(
        cells.cell_centers().points,
        labels=[f"{i}" for i in ids],
    )

    # Add other cells
    ids.append(i_cell)
    others = mesh.extract_cells(ids, invert=True)
    _ = pl.add_mesh(others, show_edges=True)
pl.show()
