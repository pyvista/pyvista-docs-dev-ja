# Create a ParametricHenneberg mesh.
#
import pyvista as pv
mesh = pv.ParametricHenneberg()
mesh.plot(color='w', smooth_shading=True)
