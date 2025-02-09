from pyvista import examples
dataset = examples.download_unstructured_grid()
dataset.plot(show_edges=True)
#
# .. seealso::
#
#     :ref:`Unstructured Grid Dataset <unstructured_grid_dataset>`
