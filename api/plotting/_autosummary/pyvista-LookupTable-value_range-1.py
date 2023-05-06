# Show the effect of setting the value range on the default color
# map.
#
import pyvista as pv
lut = pv.LookupTable()
lut.value_range = (0, 1.0)
lut.plot()
#
# Demonstrate a different value range.
#
import pyvista as pv
lut = pv.LookupTable()
lut.value_range = (0.5, 0.8)
lut.plot()
