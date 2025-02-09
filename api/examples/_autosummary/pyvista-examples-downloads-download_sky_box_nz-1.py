from pyvista import examples
dataset = examples.download_sky_box_nz()
dataset.plot(rgba=True, cpos='xy')
#
# .. seealso::
#
#     :ref:`Sky Box Nz Dataset <sky_box_nz_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Sky Box Nz Texture Dataset <sky_box_nz_texture_dataset>`
