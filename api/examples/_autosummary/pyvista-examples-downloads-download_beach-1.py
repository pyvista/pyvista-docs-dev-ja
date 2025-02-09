from pyvista import examples
dataset = examples.download_beach()
dataset.plot(rgba=True, cpos='xy')
#
# .. seealso::
#
#     :ref:`Beach Dataset <beach_dataset>`
