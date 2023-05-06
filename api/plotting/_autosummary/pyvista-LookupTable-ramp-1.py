# Show the default s-curve ramp.
#
import pyvista as pv
lut = pv.LookupTable()
lut.hue_range = (0.0, 0.33)
lut.ramp = 's-curve'
lut.plot()
#
# Plot the linear ramp.
#
import pyvista as pv
lut = pv.LookupTable()
lut.hue_range = (0.0, 0.33)
lut.ramp = 'linear'
lut.plot()
#
# Plot the ``"sqrt"`` ramp.
#
import pyvista as pv
lut = pv.LookupTable()
lut.hue_range = (0.0, 0.33)
lut.ramp = 'sqrt'
lut.plot()
