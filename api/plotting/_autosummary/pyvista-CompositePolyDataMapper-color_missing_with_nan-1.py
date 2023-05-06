# Enable coloring missing values with NaN.
#
import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
dataset[0].point_data['data'] = dataset[0].points[:, 2]
pl = pv.Plotter()
actor, mapper = pl.add_composite(
    dataset, scalars='data', show_scalar_bar=False
)
mapper.nan_color = 'r'
mapper.color_missing_with_nan = True
pl.show()
