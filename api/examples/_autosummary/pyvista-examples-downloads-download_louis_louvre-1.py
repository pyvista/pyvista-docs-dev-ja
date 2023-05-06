# Plot the Louis XIV statue with custom lighting and camera angle.
#
from pyvista import examples
import pyvista
dataset = examples.download_louis_louvre()
pl = pyvista.Plotter(lighting=None)
_ = pl.add_mesh(dataset, smooth_shading=True)
pl.add_light(pyvista.Light((10, -10, 10)))
pl.camera_position = [
    [-6.71, -14.55, 15.17],
    [1.44, 2.54, 9.84],
    [0.16, 0.22, 0.96],
]
pl.show()
