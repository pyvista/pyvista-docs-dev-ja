import pyvista as pv
lut = pv.LookupTable()
tf = lut.to_color_tf()
tf
# Expected:
## <vtkmodules.vtkRenderingCore.vtkColorTransferFunction(...) at ...>
