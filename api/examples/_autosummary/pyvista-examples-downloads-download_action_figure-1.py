# Show the action figure example. This also demonstrates how to use
# physically based rendering and lighting to make a good looking
# plot.
#
import pyvista as pv
from pyvista import examples
dataset = examples.download_action_figure()
_ = dataset.clean(inplace=True)
pl = pv.Plotter(lighting=None)
pl.add_light(pv.Light((30, 10, 10)))
_ = pl.add_mesh(
    dataset,
    color='w',
    smooth_shading=True,
    pbr=True,
    metallic=0.3,
    roughness=0.5,
)
pl.camera_position = [
    (32.3, 116.3, 220.6),
    (-0.05, 3.8, 33.8),
    (-0.017, 0.86, -0.51),
]
pl.show()
