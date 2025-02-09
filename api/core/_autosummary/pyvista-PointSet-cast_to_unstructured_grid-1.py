# Cast a :class:`pyvista.PointSet` to a
# :class:`pyvista.UnstructuredGrid`.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_cloud_dark_matter()
type(mesh)
# Expected:
## <class 'pyvista.core.pointset.PointSet'>
grid = mesh.cast_to_unstructured_grid()
type(grid)
# Expected:
## <class 'pyvista.core.pointset.UnstructuredGrid'>
