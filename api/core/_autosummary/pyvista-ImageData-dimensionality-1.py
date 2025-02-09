# Get the dimensionality of a uniform grid with dimensions ``(1, 2, 3)``.
#
import pyvista as pv
grid = pv.ImageData(dimensions=(2, 3, 4))
grid.dimensionality
# Expected:
## 3
