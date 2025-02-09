# Download and plot equivalent cell stress.
#
from pyvista import examples
grid = examples.download_fea_bracket()
grid.plot()
#
# Plot the point stress using the ``'jet'`` color map. Convert the cell data
# to point data.
#
from pyvista import examples
grid = examples.download_fea_bracket()
grid = grid.cell_data_to_point_data()
grid.plot(smooth_shading=True, split_sharp_edges=True, cmap='jet')
#
# .. seealso::
#
#     :ref:`Fea Bracket Dataset <fea_bracket_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Fea Hertzian Contact Cylinder Dataset <fea_hertzian_contact_cylinder_dataset>`
#
#     :ref:`Aero Bracket Dataset <aero_bracket_dataset>`
#
#     :ref:`Notch Stress Dataset <notch_stress_dataset>`
