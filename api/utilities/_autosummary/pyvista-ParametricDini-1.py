# Create a ParametricDini mesh.
#
import pyvista as pv
mesh = pv.ParametricDini()
mesh.plot(color='w', smooth_shading=True)
