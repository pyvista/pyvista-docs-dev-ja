import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).type
# Expected:
## <CellType.TRIANGLE: 5>
