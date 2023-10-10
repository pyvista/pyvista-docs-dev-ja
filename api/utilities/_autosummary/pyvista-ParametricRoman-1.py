# Create a ParametricRoman mesh.
#
import pyvista as pv
mesh = pv.ParametricRoman()
mesh.plot(color='w', smooth_shading=True)
