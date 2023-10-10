# Clear all arrays from a mesh.
#
import pyvista as pv
import numpy as np
mesh = pv.Sphere()
mesh.point_data.keys()
# Expected:
## ['Normals']
mesh.clear_data()
mesh.point_data.keys()
# Expected:
## []
