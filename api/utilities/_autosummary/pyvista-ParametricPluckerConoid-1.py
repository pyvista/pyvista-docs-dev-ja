# Create a ParametricPluckerConoid mesh.
#
import pyvista as pv
mesh = pv.ParametricPluckerConoid()
mesh.plot(color='w', smooth_shading=True)
