# Create a ParametricBohemianDome mesh.
#
import pyvista as pv
mesh = pv.ParametricBohemianDome()
mesh.plot(color='w', smooth_shading=True)
