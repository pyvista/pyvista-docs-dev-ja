import pyvista
lut = pyvista.LookupTable()
tf = lut.to_color_tf()
tf
# Expected:
## <vtkmodules.vtkRenderingCore.vtkColorTransferFunction(...) at ...>
