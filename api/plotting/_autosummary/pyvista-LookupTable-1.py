# Plot the lookup table with the default VTK color map.
#
import pyvista as pv
lut = pv.LookupTable()
lut
# Expected:
## LookupTable (...)
##   Table Range:                (0.0, 1.0)
##   N Values:                   256
##   Above Range Color:          None
##   Below Range Color:          None
##   NAN Color:                  Color(name='maroon', hex='#800000ff', opacity=255)
##   Log Scale:                  False
##   Color Map:                  "PyVista Lookup Table"
##     Alpha Range:              (1.0, 1.0)
##     Hue Range:                (0.0, 0.66667)
##     Saturation Range          (1.0, 1.0)
##     Value Range               (1.0, 1.0)
##     Ramp                      s-curve
lut.plot()
#
# Plot the lookup table with the ``'inferno'`` color map.
#
import pyvista as pv
lut = pv.LookupTable('inferno', n_values=32)
lut
# Expected:
## LookupTable (...)
##   Table Range:                (0.0, 1.0)
##   N Values:                   32
##   Above Range Color:          None
##   Below Range Color:          None
##   NAN Color:                  Color(name='maroon', hex='#800000ff', opacity=255)
##   Log Scale:                  False
##   Color Map:                  "inferno"
lut.plot()
