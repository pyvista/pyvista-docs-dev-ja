from pyvista import examples
dataset = examples.download_bird()
dataset.plot(rgba=True, cpos='xy')
#
# .. seealso::
#
#     :ref:`Bird Dataset <bird_dataset>`
#         See this dataset in the Dataset Gallery for more info.
