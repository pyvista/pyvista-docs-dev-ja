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
