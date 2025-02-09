# Create a small 2D grayscale image with dimensions ``3 x 2`` for demonstration.
#
import pyvista as pv
import numpy as np
from pyvista import examples
image = pv.ImageData(dimensions=(3, 2, 1))
image.point_data['data'] = np.linspace(0, 255, 6, dtype=np.uint8)
#
# Define a custom plotter to show the image. Although the image data is defined
# as point data, we use uses :meth:`points_to_cells` to display the image as
# :attr:`~pyvista.CellType.PIXEL` (or :attr:`~pyvista.CellType.VOXEL`) cells
# instead. Grayscale coloring is used and the camera is adjusted to fit the image.
#
def image_plotter(image: pv.ImageData) -> pv.Plotter:
    pl = pv.Plotter()
    image = image.points_to_cells()
    pl.add_mesh(
        image,
        lighting=False,
        show_edges=True,
        cmap='grey',
        show_scalar_bar=False,
    )
    pl.view_xy()
    pl.camera.tight()
    return pl
#
# Show the image.
#
plot = image_plotter(image)
plot.show()
#
# Use ``sample_rate`` to up-sample the image. ``'nearest'`` interpolation is
# used by default.
#
upsampled = image.resample(sample_rate=2.0)
plot = image_plotter(upsampled)
plot.show()
#
# Use ``'linear'`` interpolation. Note that the argument names ``sample_rate``
# and ``interpolation`` may be omitted.
#
upsampled = image.resample(2.0, 'linear')
plot = image_plotter(upsampled)
plot.show()
#
# Use ``'cubic'`` interpolation. Here we also specify the output
# ``dimensions`` explicitly instead of using ``sample_rate``.
#
upsampled = image.resample(dimensions=(6, 4, 1), interpolation='cubic')
plot = image_plotter(upsampled)
plot.show()
#
# Compare the relative physical size of the image before and after resampling.
#
image
# Expected:
## ImageData (...)
##   N Cells:      2
##   N Points:     6
##   X Bounds:     0.000e+00, 2.000e+00
##   Y Bounds:     0.000e+00, 1.000e+00
##   Z Bounds:     0.000e+00, 0.000e+00
##   Dimensions:   3, 2, 1
##   Spacing:      1.000e+00, 1.000e+00, 1.000e+00
##   N Arrays:     1
#
upsampled
# Expected:
## ImageData (...)
##   N Cells:      15
##   N Points:     24
##   X Bounds:     -2.500e-01, 2.250e+00
##   Y Bounds:     -2.500e-01, 1.250e+00
##   Z Bounds:     0.000e+00, 0.000e+00
##   Dimensions:   6, 4, 1
##   Spacing:      5.000e-01, 5.000e-01, 1.000e+00
##   N Arrays:     1
#
# Note that the upsampled :attr:`~pyvista.ImageData.dimensions` are doubled and
# the :attr:`~pyvista.ImageData.spacing` is halved (as expected). Also note,
# however, that the physical bounds of the input differ from the output.
# The upsampled :attr:`~pyvista.ImageData.origin` also differs:
#
image.origin
# Expected:
## (0.0, 0.0, 0.0)
upsampled.origin
# Expected:
## (-0.25, -0.25, 0.0)
#
# This is because the resampling is done with ``extend_border`` enabled by default
# which adds a half cell-width border to the image and adjusts the origin and
# spacing such that the bounds match when the image is represented as cells.
#
# Apply :meth:`points_to_cells` to the input and resampled images and show that
# the bounds match.
#
image_as_cells = image.points_to_cells()
image_as_cells.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=2.5, y_min=-0.5, y_max=1.5, z_min=0.0, z_max=0.0)
#
upsampled_as_cells = upsampled.points_to_cells()
upsampled_as_cells.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=2.5, y_min=-0.5, y_max=1.5, z_min=0.0, z_max=0.0)
#
# Plot the two images together as wireframe to visualize them. The original is in
# red, and the resampled image is in black.
#
plt = pv.Plotter()
_ = plt.add_mesh(
    image_as_cells, style='wireframe', color='red', line_width=10
)
_ = plt.add_mesh(
    upsampled_as_cells, style='wireframe', color='black', line_width=2
)
plt.view_xy()
plt.camera.tight()
plt.show()
#
# Disable ``extend_border`` to force the input and output bounds of the points
# to be the same instead.
#
upsampled = image.resample(sample_rate=2, extend_border=False)
#
# Compare the two images again.
#
image
# Expected:
## ImageData (...)
##   N Cells:      2
##   N Points:     6
##   X Bounds:     0.000e+00, 2.000e+00
##   Y Bounds:     0.000e+00, 1.000e+00
##   Z Bounds:     0.000e+00, 0.000e+00
##   Dimensions:   3, 2, 1
##   Spacing:      1.000e+00, 1.000e+00, 1.000e+00
##   N Arrays:     1
#
upsampled
# Expected:
## ImageData (...)
##   N Cells:      15
##   N Points:     24
##   X Bounds:     0.000e+00, 2.000e+00
##   Y Bounds:     0.000e+00, 1.000e+00
##   Z Bounds:     0.000e+00, 0.000e+00
##   Dimensions:   6, 4, 1
##   Spacing:      4.000e-01, 3.333e-01, 1.000e+00
##   N Arrays:     1
#
# This time the input and output bounds match without any further processing.
# Like before, the dimensions have doubled; unlike before, however, the spacing is
# not halved, but is instead smaller than half which is necessaru to ensure the
# bounds remain the same. Also unlike before, the origin is unaffected:
#
image.origin
# Expected:
## (0.0, 0.0, 0.0)
upsampled.origin
# Expected:
## (0.0, 0.0, 0.0)
#
# All the above examples are with 2D images with point data. However, the filter
# also works with 3D volumes and will also work with cell data.
#
# Convert the 2D image with point data into a 3D volume with cell data and plot
# it for context.
#
volume = image.points_to_cells(dimensionality='3D')
volume.plot(show_edges=True, cmap='grey')
#
# Up-sample the volume. Set the sampling rate for each axis separately.
#
resampled = volume.resample(sample_rate=(3.0, 2.0, 1.0))
resampled.plot(show_edges=True, cmap='grey')
#
# Alternatively, we could have set the dimensions explicitly. Since we want
# ``9 x 4 x 1`` cells along the x-y-z axes (respectively), we set the dimensions
# to ``(10, 5, 2)``, i.e. one more than the desired number of cells.
#
resampled = volume.resample(dimensions=(10, 5, 2))
resampled.plot(show_edges=True, cmap='grey')
#
# Compare the bounds before and after resampling. Unlike with point data, the
# bounds are not (and cannot be) extended.
#
volume.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=2.5, y_min=-0.5, y_max=1.5, z_min=-0.5, z_max=0.5)
resampled.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=2.5, y_min=-0.5, y_max=1.5, z_min=-0.5, z_max=0.5)
#
# Use a reference image to control the resampling instead. Here we load two
# images with different dimensions:
# :func:`~pyvista.examples.downloads.download_puppy` and
# :func:`~pyvista.examples.downloads.download_gourds`.
#
puppy = examples.download_puppy()
puppy.dimensions
# Expected:
## (1600, 1200, 1)
#
gourds = examples.download_gourds()
gourds.dimensions
# Expected:
## (640, 480, 1)
#
# Use ``reference_image`` to resample the puppy to match the gourds geometry or
# vice-versa.
#
puppy_resampled = puppy.resample(reference_image=gourds)
puppy_resampled.dimensions
# Expected:
## (640, 480, 1)
#
gourds_resampled = gourds.resample(reference_image=puppy)
gourds_resampled.dimensions
# Expected:
## (1600, 1200, 1)
#
# Downsample the puppy image to 1/10th its original resolution using ``'lanczos'``
# interpolation.
#
downsampled = puppy.resample(0.1, 'lanczos')
downsampled.dimensions
# Expected:
## (160, 120, 1)
#
# Compare the downsampled image to the original and zoom in to show detail.
#
def compare_images_plotter(image1, image2):
    plt = pv.Plotter(shape=(1, 2))
    _ = plt.add_mesh(image1, rgba=True, show_edges=False, lighting=False)
    plt.subplot(0, 1)
    _ = plt.add_mesh(image2, rgba=True, show_edges=False, lighting=False)
    plt.link_views()
    plt.view_xy()
    plt.camera.zoom(3.0)
    return plt
#
plt = compare_images_plotter(puppy, downsampled)
plt.show()
#
# Note that downsampling can create image artifacts caused by aliasing. Enable
# anti-aliasing to smooth the image before resampling.
#
downsampled2 = puppy.resample(0.1, 'lanczos', anti_aliasing=True)
#
# Compare down-sampling with aliasing (left) to without aliasing (right).
#
plt = compare_images_plotter(downsampled, downsampled2)
plt.show()
