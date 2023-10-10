# Cast a :class:`pyvista.PolyData` to a
# :class:`pyvista.UnstructuredGrid`.
#
import pyvista as pv
mesh = pv.Sphere()
type(mesh)
# Expected:
## <class 'pyvista.core.pointset.PolyData'>
grid = mesh.cast_to_unstructured_grid()
type(grid)
# Expected:
## <class 'pyvista.core.pointset.UnstructuredGrid'>
