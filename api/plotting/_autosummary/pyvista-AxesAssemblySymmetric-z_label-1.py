# Set the labels with a single string. Plus ``'+'`` and minus ``'-'``
# characters are added automatically.
#
import pyvista as pv
axes_assembly = pv.AxesAssemblySymmetric()
axes_assembly.z_label = 'Axis'
axes_assembly.z_label
# Expected:
## ('+Axis', '-Axis')
#
# Set the labels explicitly with two strings.
#
axes_assembly.z_label = 'superior', 'inferior'
axes_assembly.z_label
# Expected:
## ('superior', 'inferior')
