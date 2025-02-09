# Shrink and plot the dataset to show it is composed of several
# tetrahedrons.
#
from pyvista import examples
dataset = examples.download_tetrahedron()
dataset.shrink(0.85).plot()
#
# .. seealso::
#
#     :ref:`Tetrahedron Dataset <tetrahedron_dataset>`
