# Disable interpolation before mapping.
#
import pyvista as pv
dataset = pv.MultiBlock([pv.Cube(), pv.Sphere(center=(0, 0, 1))])
dataset[0].point_data['data'] = dataset[0].points[:, 2]
dataset[1].point_data['data'] = dataset[1].points[:, 2]
pl = pv.Plotter()
actor, mapper = pl.add_composite(
    dataset,
    show_scalar_bar=False,
    n_colors=3,
    cmap='bwr',
)
mapper.interpolate_before_map = False
pl.show()
#
# Enable interpolation before mapping.
#
pl = pv.Plotter()
actor, mapper = pl.add_composite(
    dataset,
    show_scalar_bar=False,
    n_colors=3,
    cmap='bwr',
)
mapper.interpolate_before_map = True
pl.show()
#
# See :ref:`interpolate_before_mapping_example` for additional
