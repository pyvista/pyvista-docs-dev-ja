# Plot the example CGNS dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_cgns_structured()
dataset[0].plot(scalars='Density')
#
# .. seealso::
#
#     :ref:`Cgns Structured Dataset <cgns_structured_dataset>`
#         See this dataset in the Dataset Gallery for more info.
