# Create a ParametricKuen mesh.
#
import pyvista as pv
mesh = pv.ParametricKuen()
mesh.plot(color='w', smooth_shading=True)
