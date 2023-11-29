# Sort segmented image labels.
#
# Load image labels
#
from pyvista import examples
import numpy as np
image_labels = examples.download_frog_tissue()
#
# Show label info for first four labels
#
label_number, label_size = np.unique(
    image_labels['MetaImage'], return_counts=True
)
label_number[:4]
# Expected:
## pyvista_ndarray([0, 1, 2, 3], dtype=uint8)
label_size[:4]
# Expected:
## array([30805713,    35279,    19172,    38129])
#
# Sort labels
#
sorted_labels = image_labels.sort_labels()
#
# Show sorted label info for the four largest labels. Note
# the difference in label size after sorting.
#
sorted_label_number, sorted_label_size = np.unique(
    sorted_labels["packed_labels"], return_counts=True
)
sorted_label_number[:4]
# Expected:
## pyvista_ndarray([0, 1, 2, 3], dtype=uint8)
sorted_label_size[:4]
# Expected:
## array([30805713,   438052,   204672,   133880])
