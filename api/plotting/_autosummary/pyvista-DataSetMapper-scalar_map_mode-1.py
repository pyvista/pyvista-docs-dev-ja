# Show that the scalar map mode is set to ``'point'`` when setting the
# active scalars to point data.
#
import pyvista as pv
dataset = pv.MultiBlock([pv.Cube(), pv.Sphere(center=(0, 0, 1))])
dataset[0].point_data['data'] = dataset[0].points[:, 2]
dataset[1].point_data['data'] = dataset[1].points[:, 2]
pl = pv.Plotter()
actor, mapper = pl.add_composite(
    dataset, scalars='data', show_scalar_bar=False
)
mapper.scalar_map_mode
# Expected:
## 'point'
pl.close()
