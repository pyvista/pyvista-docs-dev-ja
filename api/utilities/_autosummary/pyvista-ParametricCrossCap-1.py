# Create a ParametricCrossCap mesh.
#
import pyvista as pv
mesh = pv.ParametricCrossCap()
mesh.plot(color='w', smooth_shading=True)
