import pyvista as pv
from pyvista import examples
grid = examples.load_explicit_structured()
cell = grid.extract_cells(31)
ind = grid.neighbors(31)
neighbors = grid.extract_cells(ind)
plotter = pv.Plotter()
_ = plotter.add_axes()
_ = plotter.add_mesh(cell, color='r', show_edges=True)
_ = plotter.add_mesh(neighbors, color='w', show_edges=True)
plotter.show()
