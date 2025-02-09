from pyvista import examples
dataset = examples.download_filled_contours()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Filled Contours Dataset <filled_contours_dataset>`
