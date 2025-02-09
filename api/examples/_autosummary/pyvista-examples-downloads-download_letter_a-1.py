from pyvista import examples
dataset = examples.download_letter_a()
dataset.plot(cpos='xy', show_edges=True)
#
# .. seealso::
#
#     :ref:`Letter A Dataset <letter_a_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Letter K Dataset <letter_k_dataset>`
#
#     :ref:`cell_centers_example`
