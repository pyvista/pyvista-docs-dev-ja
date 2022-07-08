# Plot the example Tecplot dataset.
#
from pyvista import examples
import pyvista
dataset = examples.download_tecplot_ascii()
dataset.plot()
