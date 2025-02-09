# Generate the default faces of a cube.
#
import pyvista as pv
from pyvista import examples
cube_faces_source = pv.CubeFacesSource()
output = cube_faces_source.output
output.plot(show_edges=True, line_width=10)
#
# The output is similar to that of :class:`CubeSource` except it's a
# :class:`~pyvista.MultiBlock`.
#
output
# Expected:
## MultiBlock (...)
##   N Blocks:   6
##   X Bounds:   -5.000e-01, 5.000e-01
##   Y Bounds:   -5.000e-01, 5.000e-01
##   Z Bounds:   -5.000e-01, 5.000e-01
#
cube_source = pv.CubeSource()
cube_source.output
# Expected:
## PolyData (...)
##   N Cells:    6
##   N Points:   24
##   N Strips:   0
##   X Bounds:   -5.000e-01, 5.000e-01
##   Y Bounds:   -5.000e-01, 5.000e-01
##   Z Bounds:   -5.000e-01, 5.000e-01
##   N Arrays:   2
#
# Use :attr:`explode_factor` to explode the faces.
#
cube_faces_source.explode_factor = 0.5
cube_faces_source.update()
output.plot(show_edges=True, line_width=10)
#
# Use :attr:`shrink_factor` to also shrink the faces.
#
cube_faces_source.shrink_factor = 0.5
cube_faces_source.update()
output.plot(show_edges=True, line_width=10)
#
# Fit cube faces to a dataset and only plot four of them.
#
mesh = examples.load_airplane()
cube_faces_source = pv.CubeFacesSource(bounds=mesh.bounds)
output = cube_faces_source.output
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='tomato')
_ = pl.add_mesh(output['+X'], opacity=0.5)
_ = pl.add_mesh(output['-X'], opacity=0.5)
_ = pl.add_mesh(output['+Y'], opacity=0.5)
_ = pl.add_mesh(output['-Y'], opacity=0.5)
pl.show()
#
# Generate a frame instead of full faces.
#
mesh = pv.ParametricEllipsoid(5, 4, 3)
cube_faces_source = pv.CubeFacesSource(bounds=mesh.bounds, frame_width=0.1)
output = cube_faces_source.output
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='tomato')
_ = pl.add_mesh(output, show_edges=True, line_width=10)
pl.show()
