import pyvista as pv
from pyvista import examples
import vtk
#
# Create an empty grid
#
grid = pv.UnstructuredGrid()
#
# Copy a vtk.vtkUnstructuredGrid
#
vtkgrid = vtk.vtkUnstructuredGrid()
grid = pv.UnstructuredGrid(vtkgrid)
#
# From a filename.
#
grid = pv.UnstructuredGrid(examples.hexbeamfile)
grid.plot(show_edges=True)
#
# From arrays. Here we create a single tetrahedron.
#
cells = [4, 0, 1, 2, 3]
celltypes = [pv.CellType.TETRA]
points = [
    [1.0, 1.0, 1.0],
    [1.0, -1.0, -1.0],
    [-1.0, 1.0, -1.0],
    [-1.0, -1.0, 1.0],
]
grid = pv.UnstructuredGrid(cells, celltypes, points)
grid.plot(show_edges=True)
#
# See the :ref:`create_unstructured_example` example for more details
