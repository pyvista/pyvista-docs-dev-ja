# Create a sample :class:`pyvista.ImageData` dataset.
#
import numpy as np
import pyvista as pv
n = 21
c = -(n - 1) / 2
vol = pv.ImageData(dimensions=(n, n, n), origin=(c, c, c))
scalars = np.linalg.norm(vol.points, axis=1)
scalars *= 255 / scalars.max()
vol['scalars'] = scalars
#
# Demonstrate nearest (default) interpolation.
#
pl = pv.Plotter()
actor = pl.add_volume(
    vol,
    show_scalar_bar=False,
    opacity=[0.3, 0.0, 0.05, 0.0, 0.0, 0.0, 1.0, 0.0],
    cmap='plasma',
)
actor.prop.interpolation_type = 'nearest'
pl.show()
#
# Demonstrate linear interpolation.
#
pl = pv.Plotter()
actor = pl.add_volume(
    vol,
    show_scalar_bar=False,
    opacity=[0.3, 0.0, 0.05, 0.0, 0.0, 0.0, 1.0, 0.0],
    cmap='plasma',
)
actor.prop.interpolation_type = 'linear'
pl.show()
