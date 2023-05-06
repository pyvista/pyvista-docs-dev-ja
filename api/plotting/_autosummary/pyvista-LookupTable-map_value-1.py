import pyvista
lut = pyvista.LookupTable()
rgba_color = lut.map_value(0.0)
rgba_color
# Expected:
## (1.0, 0.0, 0.0, 1.0)
