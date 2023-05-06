# Apply a user defined custom opacity to a lookup table and plot the
# random hills example.
#
import pyvista as pv
from pyvista import examples
mesh = examples.load_random_hills()
lut = pv.LookupTable(cmap='viridis')
lut.apply_opacity([1.0, 0.4, 0.0, 0.4, 0.9])
lut.scalar_range = (
    mesh.active_scalars.min(),
    mesh.active_scalars.max(),
)
pl = pv.Plotter()
_ = pl.add_mesh(mesh, cmap=lut)
pl.show()
