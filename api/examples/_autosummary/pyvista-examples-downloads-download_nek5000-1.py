from pyvista import examples
dataset = examples.download_nek5000()
dataset.plot(scalars='Velocity', cpos='xy')
#
# .. seealso::
#
#     :ref:`Nek5000 Dataset <nek5000_dataset>`
