# Create a ParametricBoy mesh.
#
import pyvista as pv
mesh = pv.ParametricBoy()
mesh.plot(color='w', smooth_shading=True)
