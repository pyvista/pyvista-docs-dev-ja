# Set the below range opacity to ``0.5``.
#
import pyvista as pv
lut = pv.LookupTable()
lut.below_range_color = 'grey'
lut.below_range_opacity = 0.5
lut.plot()
