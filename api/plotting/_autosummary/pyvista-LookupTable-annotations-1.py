# Assign annotations to the lookup table.
#
import pyvista as pv
lut = pv.LookupTable('magma')
lut.annotations = {0: 'low', 0.5: 'medium', 1: 'high'}
lut.plot()
