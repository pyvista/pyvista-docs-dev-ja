# Create a ParametricMobius mesh.
#
import pyvista as pv
mesh = pv.ParametricMobius()
mesh.plot(color='w', smooth_shading=True)
