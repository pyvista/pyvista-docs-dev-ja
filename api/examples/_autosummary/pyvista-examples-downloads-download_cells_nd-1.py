from pyvista import examples
dataset = examples.download_cells_nd()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`CellsNd Dataset <cells_nd_dataset>`
