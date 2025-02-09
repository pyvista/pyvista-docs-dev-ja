# Prepare a segmented grid.
#
import pyvista as pv
segmented_grid = pv.ImageData(dimensions=(4, 3, 3))
segmented_grid.cell_data['Data'] = [
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    2,
    0,
    0,
    0,
    0,
]
segmented_grid.plot(show_edges=True)
#
# Label the connected regions. The cells with a ``0`` value are excluded from the
# connected regions and labelled with ``0``. The remaining cells define 3 different
# regions that are labelled by decreasing size.
#
connected, labels, sizes = segmented_grid.label_connectivity(
    scalar_range='foreground'
)
pl = pv.Plotter()
_ = pl.add_mesh(connected.threshold(0.5), show_edges=True)
_ = pl.add_mesh(
    connected.threshold(0.5, invert=True),
    show_edges=True,
    opacity=0.5,
)
pl.show()
#
# Exclude the cell with a ``2`` value.
#
connected, labels, sizes = segmented_grid.label_connectivity(
    scalar_range=[1, 1]
)
pl = pv.Plotter()
_ = pl.add_mesh(connected.threshold(0.5), show_edges=True)
_ = pl.add_mesh(
    connected.threshold(0.5, invert=True),
    show_edges=True,
    opacity=0.5,
)
pl.show()
#
# Label all connected regions with a constant value.
#
connected, labels, sizes = segmented_grid.label_connectivity(
    scalar_range='foreground',
    label_mode='constant',
    constant_value=10,
)
pl = pv.Plotter()
_ = pl.add_mesh(connected.threshold(0.5), show_edges=True)
_ = pl.add_mesh(
    connected.threshold(0.5, invert=True),
    show_edges=True,
    opacity=0.5,
)
pl.show()
#
# Label only the regions that include seed points, by seed order.
#
points = [(2.0, 1.0, 0.0), (0.0, 0.0, 1.0)]
connected, labels, sizes = segmented_grid.label_connectivity(
    scalar_range='foreground',
    extraction_mode='seeded',
    point_seeds=points,
)
pl = pv.Plotter()
_ = pl.add_mesh(connected.threshold(0.5), show_edges=True)
_ = pl.add_mesh(
    connected.threshold(0.5, invert=True),
    show_edges=True,
    opacity=0.5,
)
pl.show()
