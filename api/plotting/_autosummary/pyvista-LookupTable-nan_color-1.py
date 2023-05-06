# Set the NAN color to ``'grey'``.
#
import pyvista as pv
lut = pv.LookupTable()
lut.nan_color = 'grey'
lut.plot()
