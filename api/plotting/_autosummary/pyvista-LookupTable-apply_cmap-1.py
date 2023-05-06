# Apply ``matplotlib``'s ``'cividis'`` color map.
#
import pyvista as pv
lut = pv.LookupTable()
lut.apply_cmap('cividis', n_values=32)
lut.plot()
