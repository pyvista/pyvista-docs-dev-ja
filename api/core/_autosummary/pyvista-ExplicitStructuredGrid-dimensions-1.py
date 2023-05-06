from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
grid.dimensions  # doctest:+SKIP
# Expected:
## (5, 6, 7)
