# Set the hue range. This allows you to create a lookup table
# without setting a color map.
#
import pyvista as pv
lut = pv.LookupTable()
lut.hue_range = (0, 0.1)
lut.plot()
#
# Create a different color map.
#
import pyvista as pv
lut = pv.LookupTable()
lut.hue_range = (0.5, 0.8)
lut.plot()
