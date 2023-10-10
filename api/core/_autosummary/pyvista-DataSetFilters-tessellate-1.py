# First, plot the high order FEM-like elements.
#
import pyvista as pv
import numpy as np
points = np.array(
    [
        [0.0, 0.0, 0.0],
        [2.0, 0.0, 0.0],
        [1.0, 2.0, 0.0],
        [1.0, 0.5, 0.0],
        [1.5, 1.5, 0.0],
        [0.5, 1.5, 0.0],
    ]
)
cells = np.array([6, 0, 1, 2, 3, 4, 5])
cell_types = np.array([69])
mesh = pv.UnstructuredGrid(cells, cell_types, points)
mesh.plot(show_edges=True, line_width=5)
#
# Now, plot the tessellated mesh.
#
tessellated = mesh.tessellate()
tessellated.clear_data()  # cleans up plot
tessellated.plot(show_edges=True, line_width=5)
