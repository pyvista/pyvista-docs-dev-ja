# Create a custom "blues" lookup table that increases in saturation.
#
import pyvista as pv
lut = pv.LookupTable()
lut.hue_range = (0.7, 0.7)
lut.saturation_range = (0.0, 1.0)
lut.plot(background='grey')
