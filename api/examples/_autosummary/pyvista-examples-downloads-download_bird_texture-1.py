from pyvista import examples
dataset = examples.download_bird_texture()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Bird Texture Dataset <bird_texture_dataset>`
#         See this dataset in the Dataset Gallery for more info.
