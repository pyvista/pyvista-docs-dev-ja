# Compute the threshold of this dataset.
#
from pyvista import examples
dataset = examples.download_rectilinear_grid()
dataset.threshold(0.0001).plot()
