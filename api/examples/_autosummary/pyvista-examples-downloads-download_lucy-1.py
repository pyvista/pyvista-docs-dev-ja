# Plot the Lucy Angel dataset with custom lighting.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_lucy()
#
# Create a light at the "flame".
#
flame_light = pv.Light(
    color=[0.886, 0.345, 0.133],
    position=[550, 140, 950],
    intensity=1.5,
    positional=True,
    cone_angle=90,
    attenuation_values=(0.001, 0.005, 0),
)
#
# Create a scene light.
#
scene_light = pv.Light(intensity=0.2)
#
pl = pv.Plotter(lighting=None)
_ = pl.add_mesh(dataset, smooth_shading=True)
pl.add_light(flame_light)
pl.add_light(scene_light)
pl.background_color = 'k'
pl.show()
#
# .. seealso::
#
#     :ref:`Lucy Dataset <lucy_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`jupyter_plotting`
