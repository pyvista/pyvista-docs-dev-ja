# Plot by part ID.
#
import numpy as np
import pyvista as pv
from pyvista import examples
grid = examples.download_fea_hertzian_contact_cylinder()
grid.plot(
    scalars='PartID', cmap=['green', 'blue'], show_scalar_bar=False
)
#
# Plot the absolute value of the component stress in the Z direction.
#
pl = pv.Plotter()
z_stress = np.abs(grid['Stress'][:, 2])
_ = pl.add_mesh(
    grid,
    scalars=z_stress,
    clim=[0, 1.2e9],
    cmap='jet',
    lighting=True,
    show_edges=False,
    ambient=0.2,
)
pl.camera_position = 'xz'
pl.camera.zoom(1.4)
pl.show()
