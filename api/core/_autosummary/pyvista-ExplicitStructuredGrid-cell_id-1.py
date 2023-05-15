from pyvista import examples
grid = examples.load_explicit_structured()
grid.cell_id((3, 4, 0))
# Expected:
## 19
#
coords = [(3, 4, 0), (3, 2, 1), (1, 0, 2), (2, 3, 2)]
grid.cell_id(coords)
# Expected:
## array([19, 31, 41, 54])
