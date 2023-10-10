# Create a ParametricSuperToroid mesh.
#
import pyvista as pv
mesh = pv.ParametricSuperToroid(n1=2, n2=0.3)
mesh.plot(color='w', smooth_shading=True)
