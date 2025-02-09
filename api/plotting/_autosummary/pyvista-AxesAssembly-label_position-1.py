import pyvista as pv
axes_assembly = pv.AxesAssembly()
axes_assembly.label_position
# Expected:
## (0.8, 0.8, 0.8)
axes_assembly.label_position = 0.3
axes_assembly.label_position
# Expected:
## (0.3, 0.3, 0.3)
axes_assembly.label_position = (0.1, 0.4, 0.2)
axes_assembly.label_position
# Expected:
## (0.1, 0.4, 0.2)
