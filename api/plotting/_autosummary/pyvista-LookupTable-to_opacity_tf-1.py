import pyvista as pv
lut = pv.LookupTable()
tf = lut.to_opacity_tf()
tf
# Expected:
## <vtkmodules.vtkCommonDataModel.vtkPiecewiseFunction(...) at ...>
