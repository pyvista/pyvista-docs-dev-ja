# Create a ParametricTorus mesh.
#
import pyvista as pv
mesh = pv.ParametricTorus()
mesh.plot(color='w', smooth_shading=True)
