# Plot the airfoil dataset. Merge the multi-block and then plot the airfoil's
# ``"ViscosityEddy"``. Convert the cell data to point data as in this
# dataset, the solution is stored within the cells.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_cgns_multi()
ugrid = dataset.combine()
ugrid = ugrid = ugrid.cell_data_to_point_data()
ugrid.plot(
    cmap='bwr',
    scalars='ViscosityEddy',
    zoom=4,
    cpos='xz',
    show_scalar_bar=False,
)
#
# .. seealso::
#
#     :ref:`Cgns Multi Dataset <cgns_multi_dataset>`
#         See this dataset in the Dataset Gallery for more info.
