# Plot the density of the air surrounding the NACA airfoil using the
# ``"jet"`` color map.
#
from pyvista import examples
cpos = [[-0.22, 0.0, 2.52], [0.43, 0.0, 0.0], [0.0, 1.0, 0.0]]
dataset = examples.download_naca()
dataset.plot(cpos=cpos, cmap='jet')
#
# .. seealso::
#
#     :ref:`Naca Dataset <naca_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`reader_example`
