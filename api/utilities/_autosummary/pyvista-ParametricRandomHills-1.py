# Create a ParametricRandomHills mesh.
#
import pyvista as pv
mesh = pv.ParametricRandomHills()
mesh.plot(color='w', smooth_shading=True)
