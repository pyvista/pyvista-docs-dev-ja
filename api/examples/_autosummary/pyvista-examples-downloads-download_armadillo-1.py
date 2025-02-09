# Plot the armadillo dataset. Use a custom camera position.
#
from pyvista import examples
cpos = [
    (161.5, 82.1, -330.2),
    (-4.3, 24.5, -1.6),
    (-0.1, 1, 0.12),
]
dataset = examples.download_armadillo()
dataset.plot(cpos=cpos)
#
# .. seealso::
#
#     :ref:`Armadillo Dataset <armadillo_dataset>`
