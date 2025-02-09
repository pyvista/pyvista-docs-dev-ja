# Set the labels with a single string. Plus ``'+'`` and minus ``'-'``
# characters are added automatically.
#
import pyvista as pv
axes_assembly = pv.AxesAssemblySymmetric()
axes_assembly.y_label = 'Axis'
axes_assembly.y_label
# Expected:
## ('+Axis', '-Axis')
#
# Set the labels explicitly with two strings.
#
axes_assembly.y_label = 'left', 'right'
axes_assembly.y_label
# Expected:
## ('left', 'right')
