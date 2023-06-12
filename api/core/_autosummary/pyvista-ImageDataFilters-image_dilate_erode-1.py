# Demonstrate image dilate/erode on an example dataset. First, plot
# the example dataset with the active scalars.
#
from pyvista import examples
uni = examples.load_uniform()
uni.plot()
#
# Now, plot the image threshold with ``threshold=[400, 600]``. Note how
# values within the threshold are 1 and outside are 0.
#
ithresh = uni.image_threshold([400, 600])
ithresh.plot()
#
# Note how there is a hole in the thresholded image. Apply a dilation/
# erosion filter with a large kernel to fill that hole in.
#
idilate = ithresh.image_dilate_erode(kernel_size=[5, 5, 5])
idilate.plot()
