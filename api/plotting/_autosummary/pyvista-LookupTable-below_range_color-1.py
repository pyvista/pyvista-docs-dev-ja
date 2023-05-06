# Enable the usage of the below range color.
#
import pyvista as pv
lut = pv.LookupTable()
lut.below_range_color = 'blue'
lut.plot()
#
# Disable the usage of the below range color.
#
import pyvista as pv
lut = pv.LookupTable()
lut.below_range_color = None
lut.plot()
