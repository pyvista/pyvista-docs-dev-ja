# Show that scalar visibility is ``False``.
#
import pyvista as pv
mesh = pv.Sphere()
pl = pv.Plotter()
actor = pl.add_mesh(mesh)
actor.mapper.scalar_visibility
# Expected:
## False
pl.close()
#
# Show that scalar visibility is ``True``.
#
import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
dataset[0].point_data['data'] = dataset[0].points[:, 2]
dataset[1].point_data['data'] = dataset[1].points[:, 2]
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset, scalars='data')
mapper.scalar_visibility
# Expected:
## True
pl.close()
