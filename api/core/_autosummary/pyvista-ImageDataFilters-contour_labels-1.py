# Load labeled image data with a background region ``0`` and four foreground
# regions.
#
import pyvista as pv
import numpy as np
from pyvista import examples
image = examples.load_channels()
label_ids = np.unique(image.active_scalars)
label_ids
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4])
image.dimensions
# Expected:
## (251, 251, 101)
#
# Crop the image to simplify the data.
#
image = image.extract_subset(voi=(75, 109, 75, 109, 85, 100))
image.dimensions
# Expected:
## (35, 35, 16)
#
# Plot the cropped image for context. Configure the color map to generate
# consistent coloring of the regions for all plots.
#
def labels_plotter(mesh, zoom=None):
    colored_mesh = mesh.color_labels(negative_indexing=True)
    plotter = pv.Plotter()
    plotter.add_mesh(colored_mesh, show_edges=True)
    if zoom:
        plotter.camera.zoom(zoom)
    return plotter
labels_plotter(image).show()
#
# Generate surface contours of the foreground regions and plot it. Note that
# the ``background_value`` is ``0`` by default.
#
contours = image.contour_labels()
labels_plotter(contours, zoom=1.5).show()
#
# By default, only external boundary polygons are generated and the returned
# ``'boundary_labels'`` array is a single-component array. The output values
# match the input label values.
#
contours['boundary_labels'].ndim
# Expected:
## 1
np.unique(contours['boundary_labels'])
# Expected:
## pyvista_ndarray([1, 2, 3, 4])
#
# Set ``simplify_output`` to ``False`` to generate a two-component
# array instead showing the two boundary regions associated with each polygon.
#
contours = image.contour_labels(simplify_output=False)
contours['boundary_labels'].ndim
# Expected:
## 2
#
# Show the unique values. Since only ``'external'`` boundaries are generated
# by default, the second component is always ``0`` (i.e. the ``background_value``).
# Note that all four foreground regions share a boundary with the background.
#
np.unique(contours['boundary_labels'], axis=0)
# Expected:
## array([[1, 0],
##        [2, 0],
##        [3, 0],
##        [4, 0]])
#
# Repeat the example but this time generate internal contours only. The generated
# array is 2D by default.
#
contours = image.contour_labels('internal')
contours['boundary_labels'].ndim
# Expected:
## 2
#
# Show the unique two-component boundary labels again. From these values we can
# determine that all foreground regions share an internal boundary with each
# other `except`  for regions ``1`` and ``3`` since the boundary value ``[1, 3]``
# is missing.
#
np.unique(contours['boundary_labels'], axis=0)
# Expected:
## array([[1, 2],
##        [1, 4],
##        [2, 3],
##        [2, 4],
##        [3, 4]])
#
# Simplify the output so that each internal multi-component boundary value is
# assigned a unique negative integer value instead. This makes it easier to
# visualize the result.
#
contours = image.contour_labels('internal', simplify_output=True)
contours['boundary_labels'].ndim
# Expected:
## 1
np.unique(contours['boundary_labels'])
# Expected:
## pyvista_ndarray([-5, -4, -3, -2, -1])
#
labels_plotter(contours, zoom=1.5).show()
#
# Generate contours for all boundaries, and use ``select_outputs`` to filter
# the output to only include polygons which share a boundary with region ``3``.
#
region_3 = image.contour_labels(
    'all', select_outputs=3, simplify_output=True
)
labels_plotter(region_3, zoom=3).show()
#
# Note how using ``select_outputs`` preserves the sharp features and boundary
# labels for non-selected regions. If desired, use ``select_inputs`` instead to
# completely "ignore" non-selected regions.
#
region_3 = image.contour_labels(select_inputs=3)
labels_plotter(region_3, zoom=3).show()
#
# The sharp features are now smoothed and the internal boundaries are now labeled
# as external boundaries. Note that using ``'all'`` here is optional since
# using ``select_inputs`` converts previously-internal boundaries into external
# ones.
#
# Do not pad the image with background values before contouring. Since the input image
# has foreground regions visible at the edges of the image (e.g. the ``+Z`` bound),
# setting ``pad_background=False`` in this example causes the top and sides of
# the mesh to be "open".
#
surf = image.contour_labels(pad_background=False)
labels_plotter(surf, zoom=1.5).show()
#
# Disable smoothing to generate staircase-like surface. Without smoothing, the
# surface has quadrilateral cells by default.
#
surf = image.contour_labels(smoothing=False)
labels_plotter(surf, zoom=1.5).show()
#
# Keep smoothing enabled but reduce the smoothing scale. A smoothing scale
# less than one may help preserve sharp features (e.g. corners).
#
surf = image.contour_labels(smoothing_scale=0.5)
labels_plotter(surf, zoom=1.5).show()
