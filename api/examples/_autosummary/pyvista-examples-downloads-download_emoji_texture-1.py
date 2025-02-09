from pyvista import examples
dataset = examples.download_emoji_texture()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Emoji Texture Dataset <emoji_texture_dataset>`
#         See this dataset in the Dataset Gallery for more info.
