# Loop over the cells
#
import pyvista as pv
mesh = pv.ImageData(dimensions=(3, 3, 1))
for cell in mesh.cell:  # doctest: +SKIP
    cell
