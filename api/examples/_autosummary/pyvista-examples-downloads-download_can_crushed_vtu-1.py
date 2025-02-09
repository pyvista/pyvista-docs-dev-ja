# Plot the crushed can dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_can_crushed_vtu()
dataset.plot(smooth_shading=True)
#
# .. seealso::
#
#     :ref:`Can Crushed Vtu Dataset <can_crushed_vtu_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Can Crushed Hdf Dataset <can_crushed_hdf_dataset>`
