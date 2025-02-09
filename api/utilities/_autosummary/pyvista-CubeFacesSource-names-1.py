import pyvista as pv
cube_faces = pv.CubeFacesSource()
#
# Use three strings to set the names. Plus ``'+'`` and minus ``'-'``
# characters are added automatically.
#
cube_faces.names = ['U', 'V', 'W']
cube_faces.names
# Expected:
## ('+U', '-U', '+V', '-V', '+W', '-W')
#
# Alternatively, use six strings to set the names explicitly.
#
cube_faces.names = [
    'right',
    'left',
    'anterior',
    'posterior',
    'superior',
    'inferior',
]
cube_faces.names
# Expected:
## ('right', 'left', 'anterior', 'posterior', 'superior', 'inferior')
