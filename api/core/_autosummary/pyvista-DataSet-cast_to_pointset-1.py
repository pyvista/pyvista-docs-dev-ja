import pyvista as pv
mesh = pv.Wavelet()
pointset = mesh.cast_to_pointset()
type(pointset)
# Expected:
## <class 'pyvista.core.pointset.PointSet'>
