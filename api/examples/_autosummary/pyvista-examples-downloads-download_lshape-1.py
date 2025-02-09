# Load and plot the dataset.
#
from pyvista import examples
mesh = examples.download_lshape()['all']
warped = mesh.warp_by_vector(factor=30)
warped.plot(scalars='displacement')
#
# .. seealso::
#
#     :ref:`Lshape Dataset <lshape_dataset>`
