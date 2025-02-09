# Display the cubemap as both an environment texture and an actor.
#
import pyvista as pv
from pyvista import examples
cubemap = examples.download_cubemap_space_4k()
pl = pv.Plotter(lighting=None)
_ = pl.add_actor(cubemap.to_skybox())
pl.set_environment_texture(cubemap, True)
pl.camera.zoom(0.4)
_ = pl.add_mesh(pv.Sphere(), pbr=True, roughness=0.24, metallic=1.0)
pl.show()
#
# .. seealso::
#
#     :ref:`Cubemap Space 4k Dataset <cubemap_space_4k_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Cubemap Space 16k Dataset <cubemap_space_16k_dataset>`
#
#     :ref:`Cubemap Park Dataset <cubemap_park_dataset>`
