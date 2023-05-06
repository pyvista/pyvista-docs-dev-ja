# Add a volume to a :class:`pyvista.Plotter` and get its mapper.
#
import pyvista as pv
vol = pv.UniformGrid(dimensions=(10, 10, 10))
vol['scalars'] = 255 - vol.z * 25
pl = pv.Plotter()
actor = pl.add_volume(vol)
actor.mapper.bounds
# Expected:
## (0.0, 9.0, 0.0, 9.0, 0.0, 9.0)
