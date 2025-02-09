import pyvista as pv
axes_assembly = pv.AxesAssemblySymmetric()
#
# Use three strings to set the labels. Plus ``'+'`` and minus ``'-'``
# characters are added automatically.
#
axes_assembly.labels = ['U', 'V', 'W']
axes_assembly.labels
# Expected:
## ('+U', '-U', '+V', '-V', '+W', '-W')
#
# Alternatively, use six strings to set the labels explicitly.
#
axes_assembly.labels = [
    'east',
    'west',
    'north',
    'south',
    'up',
    'down',
]
axes_assembly.labels
# Expected:
## ('east', 'west', 'north', 'south', 'up', 'down')
