# Plot the crushed can dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_can_crushed_hdf()
dataset.plot(smooth_shading=True)
