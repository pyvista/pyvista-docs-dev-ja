from pyvista import examples
dataset = examples.download_gourds_texture()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Gourds Texture Dataset <gourds_texture_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Gourds Dataset <gourds_dataset>`
