# Create a custom "blues" lookup table that decreases in opacity.
#
import pyvista as pv
lut = pv.LookupTable()
lut.hue_range = (0.7, 0.7)
lut.alpha_range = (1.0, 0.0)
lut.plot(background='grey')
