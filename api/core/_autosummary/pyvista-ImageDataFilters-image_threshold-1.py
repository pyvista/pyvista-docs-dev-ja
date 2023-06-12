# Demonstrate image threshold on an example dataset. First, plot
# the example dataset with the active scalars.
#
from pyvista import examples
uni = examples.load_uniform()
uni.plot()
#
# Now, plot the image threshold with ``threshold=100``. Note how
# values above the threshold are 1 and below are 0.
#
ithresh = uni.image_threshold(100)
ithresh.plot()
