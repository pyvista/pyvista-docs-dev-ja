import pyvista as pv
lut = pv.LookupTable()
lut.scalar_range = (0, 10)
lut.scalar_range
# Expected:
## (0.0, 10.0)
