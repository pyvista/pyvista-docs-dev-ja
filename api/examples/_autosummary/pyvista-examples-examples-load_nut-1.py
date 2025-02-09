# Load an example nut and plot with smooth shading.
#
from pyvista import examples
mesh = examples.load_nut()
mesh.plot(smooth_shading=True, split_sharp_edges=True)
#
# .. seealso::
#
#     :ref:`Nut Dataset <nut_dataset>`
