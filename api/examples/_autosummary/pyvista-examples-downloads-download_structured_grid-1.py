from pyvista import examples
dataset = examples.download_structured_grid()
dataset.plot(show_edges=True)
#
# .. seealso::
#
#     :ref:`Structured Grid Dataset <structured_grid_dataset>`
#         See this dataset in the Dataset Gallery for more info.
