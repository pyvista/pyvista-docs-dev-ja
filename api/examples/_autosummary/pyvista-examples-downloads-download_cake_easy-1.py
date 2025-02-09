from pyvista import examples
dataset = examples.download_cake_easy()
dataset.plot(rgba=True, cpos='xy')
#
# .. seealso::
#
#     :ref:`Cake Easy Dataset <cake_easy_dataset>`
#         See this dataset in the Dataset Gallery for more info.
