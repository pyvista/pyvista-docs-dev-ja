from pyvista import examples
grid = examples.load_explicit_structured()
grid.dimensions
# Expected:
## (5, 6, 7)
