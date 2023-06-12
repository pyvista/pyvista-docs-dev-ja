# Show a built-in volume example with the coolwarm colormap.
#
from pyvista import examples
import pyvista as pv
bolt_nut = examples.download_bolt_nut()
pl = pv.Plotter()
_ = pl.add_volume(bolt_nut, cmap="coolwarm")
pl.show()
#
# Create a volume from scratch and plot it using single vector of
# scalars.
#
import pyvista as pv
grid = pv.ImageData(dimensions=(9, 9, 9))
grid['scalars'] = -grid.x
pl = pv.Plotter()
_ = pl.add_volume(grid, opacity='linear')
pl.show()
#
# Plot a volume from scratch using RGBA scalars
#
import pyvista as pv
import numpy as np
grid = pv.ImageData(dimensions=(5, 20, 20))
scalars = grid.points - (grid.origin)
scalars /= scalars.max()
opacity = np.linalg.norm(
    grid.points - grid.center, axis=1
).reshape(-1, 1)
opacity /= opacity.max()
scalars = np.hstack((scalars, opacity**3))
scalars *= 255
pl = pv.Plotter()
vol = pl.add_volume(grid, scalars=scalars.astype(np.uint8))
vol.prop.interpolation_type = 'linear'
pl.show()
#
# Plot an UnstructuredGrid.
#
from pyvista import examples
import pyvista as pv
mesh = examples.download_letter_a()
mesh['scalars'] = mesh.points[:, 1]
pl = pv.Plotter()
_ = pl.add_volume(mesh, opacity_unit_distance=0.1)
pl.show()
