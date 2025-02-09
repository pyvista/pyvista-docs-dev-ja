from pyvista import examples
dataset = examples.download_puppy_texture()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Puppy Texture Dataset <puppy_texture_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Puppy Dataset <puppy_dataset>`
#
#     :ref:`texture_example`
