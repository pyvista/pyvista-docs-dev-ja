# Load a mesh.
#
import pyvista as pv
from pyvista import examples
mesh = examples.load_ant()
#
# Add data to the user dict. The contents are serialized as JSON.
#
mesh.user_dict['name'] = 'ant'
mesh.user_dict
# Expected:
## {"name": "ant"}
#
# Alternatively, set the user dict from an existing dict.
#
mesh.user_dict = dict(name='ant')
#
# The user dict can be updated like a regular dict.
#
mesh.user_dict.update(
    {
        'num_legs': 6,
        'body_parts': ['head', 'thorax', 'abdomen'],
    }
)
mesh.user_dict
# Expected:
## {"name": "ant", "num_legs": 6, "body_parts": ["head", "thorax", "abdomen"]}
#
# Data in the user dict is stored as field data.
#
mesh.field_data
# Expected:
## pyvista DataSetAttributes
## Association     : NONE
## Contains arrays :
##     _PYVISTA_USER_DICT      str        "{"name": "ant",..."
#
# Since it's field data, the user dict can be saved to file along with the
# mesh and retrieved later.
#
mesh.save('ant.vtk')
mesh_from_file = pv.read('ant.vtk')
mesh_from_file.user_dict
# Expected:
## {"name": "ant", "num_legs": 6, "body_parts": ["head", "thorax", "abdomen"]}
