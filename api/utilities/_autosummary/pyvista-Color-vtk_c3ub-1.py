# Create a blue color with half opacity.
#
import pyvista as pv
c = pv.Color("blue", default_opacity=0.5)
c
# Expected:
## Color(name='blue', hex='#0000ff80', opacity=128)
c.vtk_c3ub
# Expected:
## vtkmodules.vtkCommonDataModel.vtkColor3ub([0, 0, 255])
