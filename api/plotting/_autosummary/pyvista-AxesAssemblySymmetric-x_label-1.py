# Set the labels with a single string. Plus ``'+'`` and minus ``'-'``
# characters are added automatically.
#
import pyvista as pv
axes_assembly = pv.AxesAssemblySymmetric()
axes_assembly.x_label = 'Axis'
axes_assembly.x_label
# Expected:
## ('+Axis', '-Axis')
#
# Set the labels explicitly with two strings.
#
axes_assembly.x_label = 'anterior', 'posterior'
axes_assembly.x_label
# Expected:
## ('anterior', 'posterior')
