# Create a ParametricFigure8Klein mesh.
#
import pyvista as pv
mesh = pv.ParametricFigure8Klein()
mesh.plot(color='w', smooth_shading=True)
