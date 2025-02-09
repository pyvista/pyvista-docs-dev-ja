# Add field data to a PolyData dataset.
#
import pyvista as pv
import numpy as np
mesh = pv.Sphere()
mesh.add_field_data(np.arange(10), 'my-field-data')
mesh['my-field-data']
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# Add field data to a ImageData dataset.
#
mesh = pv.ImageData(dimensions=(2, 2, 1))
mesh.add_field_data(['I could', 'write', 'notes', 'here'], 'my-field-data')
mesh['my-field-data']
# Expected:
## pyvista_ndarray(['I could', 'write', 'notes', 'here'], dtype='<U7')
#
# Add field data to a MultiBlock dataset.
#
blocks = pv.MultiBlock()
blocks.append(pv.Sphere())
blocks['cube'] = pv.Cube(center=(0, 0, -1))
blocks.add_field_data([1, 2, 3], 'my-field-data')
blocks.field_data['my-field-data']
# Expected:
## pyvista_ndarray([1, 2, 3])
