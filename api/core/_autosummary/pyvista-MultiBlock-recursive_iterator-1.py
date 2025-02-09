# Load a :class:`MultiBlock` with nested datasets.
#
import pyvista as pv
from pyvista import examples
dataset = examples.download_biplane()
#
# The dataset has eight :class:`MultiBlock` blocks.
#
dataset.n_blocks
# Expected:
## 8
#
all(isinstance(block, pv.MultiBlock) for block in dataset)
# Expected:
## True
#
# Get the iterator and show the count of all recursively nested datasets.
#
iterator = dataset.recursive_iterator()
iterator
# Expected:
## <generator object MultiBlock.recursive_iterator at ...>
#
len(list(iterator))
# Expected:
## 59
#
# By default, ``None`` blocks are excluded and all items are :class:`~pyvista.DataSet`
# objects.
#
all(isinstance(item, pv.DataSet) for item in dataset.recursive_iterator())
# Expected:
## True
