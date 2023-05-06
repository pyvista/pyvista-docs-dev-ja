# Plot the ``"reds"`` colormap with 10 values.
#
import pyvista as pv
lut = pv.LookupTable('reds')
lut.n_values = 10
lut.plot()
#
# Plot the default colormap with 1024 values.
#
import pyvista as pv
lut = pv.LookupTable()
lut.n_values = 1024
lut.plot()
