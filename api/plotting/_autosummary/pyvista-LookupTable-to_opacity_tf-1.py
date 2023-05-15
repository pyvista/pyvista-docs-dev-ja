import pyvista
lut = pyvista.LookupTable()
tf = lut.to_opacity_tf()
tf
# Expected:
## <vtkmodules.vtkCommonDataModel.vtkPiecewiseFunction(...) at ...>
