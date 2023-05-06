# Load the datasets
#
import pyvista as pv
from pyvista import examples
structure, air = examples.download_electronics_cooling()
structure, air  # doctest:+SKIP
# Expected:
## (PolyData (0x7fdfe4eb24a0)
##    N Cells:    344270
##    N Points:   187992
##    N Strips:   0
##    X Bounds:   -3.000e-03, 1.530e-01
##    Y Bounds:   -3.000e-03, 2.030e-01
##    Z Bounds:   -9.000e-03, 4.200e-02
##    N Arrays:   5,
##  UnstructuredGrid (0x7fdfde4478e0)
##    N Cells:    1749992
##    N Points:   610176
##    X Bounds:   -1.388e-18, 1.500e-01
##    Y Bounds:   -3.000e-03, 2.030e-01
##    Z Bounds:   -6.000e-03, 4.400e-02
##    N Arrays:   10)
#
# Plot the air velocity through the electronics.
#
z_slice = air.clip('z', value=-0.005)
pl = pv.Plotter()
pl.enable_ssao(radius=0.01)
_ = pl.add_mesh(
    z_slice,
    scalars='U',
    lighting=False,
    scalar_bar_args={'title': 'Velocity'},
)
_ = pl.add_mesh(
    structure,
    color='w',
    smooth_shading=True,
    split_sharp_edges=True,
)
pl.camera_position = 'xy'
pl.camera.roll = 90
pl.enable_anti_aliasing('fxaa')
pl.show()
