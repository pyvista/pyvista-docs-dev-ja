import pyvista
lut = pyvista.LookupTable()
tf = lut.to_opacity_tf()
tf  # doctest:+SKIP
# Expected:
## <vtkmodules.vtkCommonDataModel.vtkPiecewiseFunction(0x32fa410) at 0x7fe963d6d5e0>
