from pyvista import examples
dataset = examples.download_puppy()
dataset.plot(cpos='xy', rgba=True)
#
# .. seealso::
#
#     :ref:`Puppy Dataset <puppy_dataset>`
#         See this dataset in the Dataset Gallery for more info.
