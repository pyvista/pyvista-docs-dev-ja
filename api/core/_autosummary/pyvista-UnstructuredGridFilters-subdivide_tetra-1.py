# First, load a sample tetrahedral UnstructuredGrid and plot it.
#
from pyvista import examples
grid = examples.load_tetbeam()
grid.plot(show_edges=True, line_width=2)
#
# Now, subdivide and plot.
#
subdivided = grid.subdivide_tetra()
subdivided.plot(show_edges=True, line_width=2)
