# Load image with labeled regions.
#
import numpy as np
import pyvista as pv
from pyvista import examples
image = examples.load_channels()
np.unique(image.active_scalars)
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4])
#
# Split the image into its separate regions. Here, we also remove the first
# region for visualization.
#
multiblock = image.split_values()
_ = multiblock.pop(0)  # Remove first region
#
# Plot the regions.
#
plot = pv.Plotter()
_ = plot.add_composite(multiblock, multi_colors=True)
_ = plot.show_grid()
plot.show()
#
# Note that the block names are generic by default.
#
multiblock.keys()
# Expected:
## ['Block-01', 'Block-02', 'Block-03', 'Block-04']
#
# To name the output blocks, use a dictionary as input instead.
#
# Here, we also explicitly omit the region with ``0`` values from the input
# instead of removing it from the output.
#
labels = dict(region1=1, region2=2, region3=3, region4=4)
multiblock = image.split_values(labels)
multiblock.keys()
# Expected:
## ['region1', 'region2', 'region3', 'region4']
#
# Plot the regions as separate meshes using the labels instead of plotting
# the MultiBlock directly.
#
# Clear scalar data so we can color each mesh using a single color
#
_ = [block.clear_data() for block in multiblock]
plot = pv.Plotter()
plot.set_color_cycler('default')
_ = [
    plot.add_mesh(block, label=label)
    for block, label in zip(multiblock, labels)
]
_ = plot.add_legend()
plot.show()
