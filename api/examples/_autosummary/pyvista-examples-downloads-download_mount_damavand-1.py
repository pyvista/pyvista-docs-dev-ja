# Download the Damavand dataset and plot it after warping it by its altitude.
#
from pyvista import examples
dataset = examples.download_mount_damavand()
dataset = dataset.cell_data_to_point_data()
dataset = dataset.warp_by_scalar('z', factor=2)
dataset.plot(cmap='gist_earth', show_scalar_bar=False)
