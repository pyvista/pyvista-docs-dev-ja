# Set the NAN opacity to ``0.5``.
#
import pyvista as pv
lut = pv.LookupTable()
lut.nan_color = 'grey'
lut.nan_opacity = 0.5
lut.plot()
