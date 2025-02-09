from pyvista import examples
dataset = examples.download_rgba_texture()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Rgba Texture Dataset <rgba_texture_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`texture_example`
