# Apply the single Matplotlib color map ``"Oranges"``.
#
import pyvista as pv
lut = pv.LookupTable()
lut.cmap = 'Oranges'
lut.plot()
#
# Apply a list of colors as a colormap.
#
import pyvista as pv
lut = pv.LookupTable()
lut.cmap = ['black', 'red', 'orange']
lut.plot()
