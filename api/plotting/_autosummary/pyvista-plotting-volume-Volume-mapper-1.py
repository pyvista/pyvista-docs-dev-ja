# Add a volume to a :class:`pyvista.Plotter` and get its mapper.
#
import pyvista as pv
vol = pv.ImageData(dimensions=(10, 10, 10))
vol['scalars'] = 255 - vol.z * 25
pl = pv.Plotter()
actor = pl.add_volume(vol)
actor.mapper.bounds
# Expected:
## BoundsTuple(x_min=0.0, x_max=9.0, y_min=0.0, y_max=9.0, z_min=0.0, z_max=9.0)
