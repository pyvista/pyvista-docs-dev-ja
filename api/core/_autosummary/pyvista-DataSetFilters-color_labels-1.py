# Load labeled data and crop it with :meth:`~pyvista.ImageDataFilters.extract_subset`
# to simplify the data.
#
from pyvista import examples
import numpy as np
image_labels = examples.load_channels()
image_labels = image_labels.extract_subset(voi=(75, 109, 75, 109, 85, 100))
#
# Plot the dataset with default coloring using a categorical color map. The
# plotter by default uniformly samples from all 256 colors in the color map based
# on the data's range.
#
image_labels.plot(cmap='glasbey_category10')
#
# Show label ids of the dataset.
#
label_ids = np.unique(image_labels.active_scalars)
label_ids
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4])
#
# Color the labels with the filter then plot them. Note that the
# ``'glasbey_category10'`` color map is used by default.
#
colored_labels = image_labels.color_labels()
colored_labels.plot()
#
# Since the labels are unsigned integers, the ``'index'`` coloring mode is used
# by default. Unlike the uniform sampling used by the plotter in the previous
# plot, the colormap is instead indexed using the label values. This ensures
# that labels have a consistent coloring regardless of the input. For example,
# we can crop the dataset further.
#
subset_labels = image_labels.extract_subset(voi=(15, 34, 28, 34, 12, 15))
#
# And show that only three labels remain.
#
label_ids = np.unique(subset_labels.active_scalars)
label_ids
# Expected:
## pyvista_ndarray([1, 2, 3])
#
# Despite the changes to the dataset, the regions have the same coloring
# as before.
#
colored_labels = subset_labels.color_labels()
colored_labels.plot()
#
# Use the ``'cycle'`` coloring mode instead to map label values to colors
# sequentially.
#
colored_labels = subset_labels.color_labels(coloring_mode='cycle')
colored_labels.plot()
#
# Map the colors explicitly using a dictionary.
#
colors = {0: 'black', 1: 'red', 2: 'lime', 3: 'blue', 4: 'yellow'}
colored_labels = image_labels.color_labels(colors)
colored_labels.plot()
#
# Omit the background value from the mapping and specify float colors. When
# floats are specified, values without a mapping are assigned ``nan`` values
# and are not plotted by default.
#
colors.pop(0)
# Expected:
## 'black'
colored_labels = image_labels.color_labels(colors, color_type='float_rgba')
colored_labels.plot()
#
# Modify the scalars and make two of the labels negative.
#
scalars = image_labels.active_scalars
scalars[scalars > 2] *= -1
np.unique(scalars)
# Expected:
## pyvista_ndarray([-4, -3,  0,  1,  2])
#
# Color the mesh and enable ``negative_indexing``. With this option enabled,
# the ``'index'`` coloring mode is used by default, and therefore the positive
# values ``0``, ``1``, and ``2`` are colored with the first, second, and third
# color in the colormap, respectively. Negative values ``-3`` and ``-4`` are
# colored with the third-last and fourth-last color in the colormap, respectively.
#
colored_labels = image_labels.color_labels(negative_indexing=True)
colored_labels.plot()
#
# If ``negative_indexing`` is disabled, the coloring defaults to the
# ``'cycle'`` coloring mode instead.
#
colored_labels = image_labels.color_labels(negative_indexing=False)
colored_labels.plot()
#
# Load the :func:`~pyvista.examples.downloads.download_foot_bones` dataset.
#
dataset = examples.download_foot_bones()
#
# Label the bones using :meth:`~pyvista.DataSetFilters.connectivity` and show
# the label values.
#
labeled_data = dataset.connectivity()
np.unique(labeled_data.active_scalars)
# Expected:
## pyvista_ndarray([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13,
##                  14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
#
# Color the dataset with default arguments. Despite having 26 separately colored
# regions, the colors from the default glasbey-style colormap are all relatively
# distinct.
#
colored_labels = labeled_data.color_labels()
colored_labels.plot()
#
# Color the mesh with fewer colors than there are label values. In this case
# the ``'cycle'`` mode is used by default and the colors are reused.
#
colored_labels = labeled_data.color_labels(['red', 'lime', 'blue'])
colored_labels.plot()
#
# Color all labels with a single color.
#
colored_labels = labeled_data.color_labels('red')
colored_labels.plot()
