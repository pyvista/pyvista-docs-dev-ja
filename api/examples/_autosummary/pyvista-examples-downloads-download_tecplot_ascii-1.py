# Plot the example Tecplot dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_tecplot_ascii()
dataset.plot()
