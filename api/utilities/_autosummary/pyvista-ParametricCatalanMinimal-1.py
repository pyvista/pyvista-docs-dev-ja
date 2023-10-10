# Create a ParametricCatalanMinimal mesh.
#
import pyvista as pv
mesh = pv.ParametricCatalanMinimal()
mesh.plot(color='w', smooth_shading=True)
