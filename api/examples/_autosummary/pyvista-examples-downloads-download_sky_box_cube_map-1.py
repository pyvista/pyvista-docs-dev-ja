from pyvista import examples
import pyvista as pv
pl = pv.Plotter()
dataset = examples.download_sky_box_cube_map()
_ = pl.add_actor(dataset.to_skybox())
pl.set_environment_texture(dataset)
pl.show()
#
# .. seealso::
#
#     :ref:`Sky Box Cube Map Dataset <sky_box_cube_map_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Cubemap Space 4k Dataset <cubemap_space_4k_dataset>`
#
#     :ref:`Cubemap Space 16k Dataset <cubemap_space_16k_dataset>`
#
#     :ref:`Cubemap Park Dataset <cubemap_park_dataset>`
#
#     :ref:`pbr_example`
