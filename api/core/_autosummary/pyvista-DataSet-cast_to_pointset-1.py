import pyvista
mesh = pyvista.Wavelet()
pointset = mesh.cast_to_pointset()
type(pointset)
# Expected:
## <class 'pyvista.core.pointset.PointSet'>
