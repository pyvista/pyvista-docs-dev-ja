import pyvista as pv
axes_assembly = pv.AxesAssembly()
axes_assembly.labels = ['X Axis', 'Y Axis', 'Z Axis']
axes_assembly.labels
# Expected:
## ('X Axis', 'Y Axis', 'Z Axis')
