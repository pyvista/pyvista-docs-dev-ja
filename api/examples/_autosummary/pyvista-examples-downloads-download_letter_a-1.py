from pyvista import examples
dataset = examples.download_letter_a()
dataset.plot(cpos="xy", show_edges=True)
#
# See :ref:`cell_centers_example` for an example using
