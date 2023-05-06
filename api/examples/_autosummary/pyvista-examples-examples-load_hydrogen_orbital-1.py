# Plot the 3dxy orbital of a hydrogen atom. This corresponds to the quantum
# numbers ``n=3``, ``l=2``, and ``m=-2``.
#
from pyvista import examples
grid = examples.load_hydrogen_orbital(3, 2, -2)
grid.plot(volume=True, opacity=[1, 0, 1], cmap='magma')
#
# See :ref:`plot_atomic_orbitals_example` for additional examples using
