# Enable the usage of the above range color.
#
import pyvista as pv
lut = pv.LookupTable()
lut.above_range_color = 'blue'
lut.plot()
#
# Disable the usage of the above range color.
#
import pyvista as pv
lut = pv.LookupTable()
lut.above_range_color = None
lut.plot()
