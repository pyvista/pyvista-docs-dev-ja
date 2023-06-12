# Return the scalar range of a mapper.
#
import pyvista as pv
mesh = pv.Sphere()
pl = pv.Plotter()
actor = pl.add_mesh(mesh, scalars=mesh.points[:, 2])
actor.mapper.scalar_range
# Expected:
## (-0.5, 0.5)
pl.close()
#
# Return the scalar range of a composite dataset. In this example it's
# set to its default value of ``(0.0, 1.0)``.
#
import pyvista as pv
dataset = pv.MultiBlock(
    [pv.Cube(), pv.Sphere(center=(0, 0, 1))]
)
pl = pv.Plotter()
actor, mapper = pl.add_composite(dataset)
mapper.scalar_range
# Expected:
## (0.0, 1.0)
pl.close()
