# Create a ParametricConicSpiral mesh.
#
import pyvista as pv
mesh = pv.ParametricConicSpiral()
mesh.plot(color='w', smooth_shading=True)
