# Plot the ``"viridis"`` colormap with the below and above colors.
#
import pyvista as pv
lut = pv.LookupTable('viridis', n_values=8)
lut.below_range_color = 'black'
lut.above_range_color = 'grey'
lut.nan_color = 'r'
lut.plot()
#
# Plot only ``"blues"`` colormap.
#
import pyvista as pv
lut = pv.LookupTable('blues', n_values=1024)
lut.plot()
