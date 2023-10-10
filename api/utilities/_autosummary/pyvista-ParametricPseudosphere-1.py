# Create a ParametricPseudosphere mesh.
#
import pyvista as pv
mesh = pv.ParametricPseudosphere()
mesh.plot(color='w', smooth_shading=True)
