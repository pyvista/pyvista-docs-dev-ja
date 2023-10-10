# Create a ParametricEllipsoid mesh.
#
import pyvista as pv
mesh = pv.ParametricEllipsoid()
mesh.plot(color='w', smooth_shading=True)
