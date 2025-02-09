from pyvista import examples
dataset = examples.download_emoji()
dataset.plot(rgba=True, cpos='xy')
#
# .. seealso::
#
#     :ref:`Emoji Dataset <emoji_dataset>`
#         See this dataset in the Dataset Gallery for more info.
