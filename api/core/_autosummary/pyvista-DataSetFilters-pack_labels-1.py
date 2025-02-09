# Pack segmented image labels.
#
# Load non-contiguous image labels
#
from pyvista import examples
import numpy as np
image_labels = examples.load_frog_tissues()
#
# Show range of labels
#
image_labels.get_data_range()
# Expected:
## (np.uint8(0), np.uint8(29))
#
# Find 'gaps' in the labels
#
label_numbers = np.unique(image_labels.active_scalars)
label_max = np.max(label_numbers)
missing_labels = set(range(label_max)) - set(label_numbers)
len(missing_labels)
# Expected:
## 4
#
# Pack labels to remove gaps
#
packed_labels = image_labels.pack_labels()
#
# Show range of packed labels
#
packed_labels.get_data_range()
# Expected:
## (np.uint8(0), np.uint8(25))
