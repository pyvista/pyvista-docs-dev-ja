from pyvista import examples
dataset = examples.download_poly_line()
dataset.plot(line_width=5)
#
# .. seealso::
#
#     :ref:`Poly Line Dataset <poly_line_dataset>`
