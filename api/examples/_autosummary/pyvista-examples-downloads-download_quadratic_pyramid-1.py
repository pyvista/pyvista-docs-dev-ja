# Shrink and plot the dataset to show it is composed of several
# pyramids.
#
from pyvista import examples
dataset = examples.download_quadratic_pyramid()
dataset.shrink(0.4).plot()
