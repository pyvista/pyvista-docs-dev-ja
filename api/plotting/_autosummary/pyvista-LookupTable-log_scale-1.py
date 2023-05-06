# Use log scale for the lookup table.
#
import pyvista as pv
lut = pv.LookupTable()
lut.log_scale = True
lut.scalar_range = (1, 100)
lut.plot()
