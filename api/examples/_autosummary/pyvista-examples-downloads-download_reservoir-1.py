# Load and plot dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_reservoir()
dataset
# Expected:
## ExplicitStructuredGrid (...)
##   N Cells:    47610
##   N Points:   58433
##   X Bounds:   3.104e+05, 3.177e+05
##   Y Bounds:   7.477e+06, 7.486e+06
##   Z Bounds:   -2.472e+03, -1.577e+03
##   N Arrays:   6
#
plot = pv.Plotter()
_ = plot.add_mesh(dataset, show_edges=True)
camera = plot.camera
camera.position = (312452, 7474760, 3507)
camera.focal_point = (314388, 7481520, -2287)
camera.up = (0.09, 0.63, 0.77)
camera.distance = 9112
camera.clipping_range = (595, 19595)
plot.show()
#
# .. seealso::
#
#     :ref:`Reservoir Dataset <reservoir_dataset>`
