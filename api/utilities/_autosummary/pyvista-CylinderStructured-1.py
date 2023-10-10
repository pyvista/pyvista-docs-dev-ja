# Default structured cylinder
#
import pyvista as pv
mesh = pv.CylinderStructured()
mesh.plot(show_edges=True)
#
# Structured cylinder with an inner radius of 1, outer of 2, with 5
# segments.
#
import numpy as np
mesh = pv.CylinderStructured(radius=np.linspace(1, 2, 5))
mesh.plot(show_edges=True)
