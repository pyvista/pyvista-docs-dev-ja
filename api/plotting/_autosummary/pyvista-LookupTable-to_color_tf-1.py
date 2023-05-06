import pyvista
lut = pyvista.LookupTable()
tf = lut.to_color_tf()
tf  # doctest:+SKIP
# Expected:
## <vtkmodules.vtkRenderingCore.vtkColorTransferFunction(0x339bd40) at 0x7ffabf634700>
