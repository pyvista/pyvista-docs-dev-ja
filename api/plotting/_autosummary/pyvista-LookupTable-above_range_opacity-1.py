# Set the above range opacity to ``0.5``.
#
import pyvista as pv
lut = pv.LookupTable()
lut.above_range_color = 'grey'
lut.above_range_opacity = 0.5
lut.plot()
