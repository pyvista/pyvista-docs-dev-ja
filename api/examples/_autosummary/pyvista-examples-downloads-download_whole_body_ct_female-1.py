# Load the dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_whole_body_ct_female()
#
# Get the names of the dataset's blocks.
#
dataset.keys()
# Expected:
## ['ct', 'segmentations', 'label_map']
#
# Get the CT image.
#
ct_image = dataset['ct']
ct_image
# Expected:
## ImageData (...)
##   N Cells:      6825870
##   N Points:     6937600
##   X Bounds:     7.500e-01, 4.778e+02
##   Y Bounds:     7.500e-01, 4.778e+02
##   Z Bounds:     7.528e-01, 8.122e+02
##   Dimensions:   160, 160, 271
##   Spacing:      3.000e+00, 3.000e+00, 3.006e+00
##   N Arrays:     1
#
# Get the segmentation label names and show the first three.
#
segmentations = dataset['segmentations']
label_names = segmentations.keys()
label_names[:3]
# Expected:
## ['adrenal_gland_left', 'adrenal_gland_right', 'aorta']
#
# Get the label map and show its data range.
#
label_map = dataset['label_map']
label_map.get_data_range()
# Expected:
## (np.uint8(0), np.uint8(117))
#
# Show the ``'names_to_colors'`` dictionary with RGB colors for each segment.
#
dataset.user_dict['names_to_colors']  # doctest: +SKIP
#
# Show the ``'names_to_ids'`` dictionary with a mapping from segment names to segment ids.
#
dataset.user_dict['names_to_ids']  # doctest: +SKIP
#
# Create a surface mesh of the segmentation labels.
#
labels_mesh = label_map.contour_labels()
#
# Color the surface using :func:`~pyvista.DataSetFilters.color_labels`. Use the
# ``'ids_to_colors'`` dictionary included with the dataset to map the colors.
#
colored_mesh = labels_mesh.color_labels(
    colors=dataset.user_dict['ids_to_colors']
)
#
# Plot the CT image and segmentation labels together.
#
pl = pv.Plotter()
_ = pl.add_volume(
    ct_image,
    cmap='bone',
    opacity='sigmoid_7',
    show_scalar_bar=False,
)
_ = pl.add_mesh(colored_mesh)
pl.view_zx()
pl.camera.up = (0, 0, 1)
pl.camera.zoom(1.3)
pl.show()
#
# .. seealso::
#
#     :ref:`anatomical_groups_example`
#         Additional examples using this dataset.
#
#     :ref:`Whole Body Ct Female Dataset <whole_body_ct_female_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Whole Body Ct Male Dataset <whole_body_ct_male_dataset>`
#         Similar dataset of a male subject.
#
#     :ref:`medical_dataset_gallery`
#         Browse other medical datasets.
#
#     :ref:`volume_with_mask_example`
