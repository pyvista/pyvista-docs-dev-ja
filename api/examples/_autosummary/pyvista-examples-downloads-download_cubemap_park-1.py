from pyvista import examples
import pyvista as pv
pl = pv.Plotter(lighting=None)
dataset = examples.download_cubemap_park()
_ = pl.add_actor(dataset.to_skybox())
pl.set_environment_texture(dataset, True)
pl.camera_position = 'xy'
pl.camera.zoom(0.4)
_ = pl.add_mesh(pv.Sphere(), pbr=True, roughness=0.1, metallic=0.5)
pl.show()
#
# .. seealso::
#
#     :ref:`Cubemap Park Dataset <cubemap_park_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Cubemap Space 4k Dataset <cubemap_space_4k_dataset>`
#
#     :ref:`Cubemap Space 16k Dataset <cubemap_space_16k_dataset>`
