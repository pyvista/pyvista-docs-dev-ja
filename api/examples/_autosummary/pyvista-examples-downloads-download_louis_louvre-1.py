# Plot the Louis XIV statue with custom lighting and camera angle.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_louis_louvre()
pl = pv.Plotter(lighting=None)
_ = pl.add_mesh(dataset, smooth_shading=True)
pl.add_light(pv.Light((10, -10, 10)))
pl.camera_position = [
    [-6.71, -14.55, 15.17],
    [1.44, 2.54, 9.84],
    [0.16, 0.22, 0.96],
]
pl.show()
#
# .. seealso::
#
#     :ref:`Louis Louvre Dataset <louis_louvre_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`pbr_example`
