from pyvista import examples
dataset = examples.download_delaunay_example()
dataset.plot(show_edges=True)
#
# .. seealso::
#
#     :ref:`Delaunay Example Dataset <delaunay_example_dataset>`
