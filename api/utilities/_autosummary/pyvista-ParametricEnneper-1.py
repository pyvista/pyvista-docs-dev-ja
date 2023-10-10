# Create a ParametricEnneper mesh.
#
import pyvista as pv
mesh = pv.ParametricEnneper()
mesh.plot(color='w', smooth_shading=True)
