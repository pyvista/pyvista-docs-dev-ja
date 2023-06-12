# Create an volume and get its properties.
#
import pyvista as pv
vol = pv.ImageData(dimensions=(10, 10, 10))
vol['scalars'] = 255 - vol.z * 25
pl = pv.Plotter()
actor = pl.add_volume(vol)
actor.prop.GetShade()
# Expected:
## 0
