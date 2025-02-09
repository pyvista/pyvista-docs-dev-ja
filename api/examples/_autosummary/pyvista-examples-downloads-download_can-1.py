# Plot the can dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_can()  # doctest:+SKIP
dataset.plot(scalars='VEL', smooth_shading=True)  # doctest:+SKIP
#
# .. seealso::
#
#     :ref:`Can Dataset <can_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Can Crushed Hdf Dataset <can_crushed_hdf_dataset>`
