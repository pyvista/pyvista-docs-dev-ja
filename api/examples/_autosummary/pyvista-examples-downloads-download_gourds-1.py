from pyvista import examples
dataset = examples.download_gourds()
dataset.plot(rgba=True, cpos='xy')
#
# .. seealso::
#
#     :ref:`Gourds Dataset <gourds_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Gourds Pnm Dataset <gourds_pnm_dataset>`
#
#     :ref:`Gourds Texture Dataset <gourds_texture_dataset>`
#
#     :ref:`gaussian_smoothing_example`
