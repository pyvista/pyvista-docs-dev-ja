# Create a ParametricKlein mesh.
#
import pyvista as pv
mesh = pv.ParametricKlein()
mesh.plot(color='w', smooth_shading=True)
