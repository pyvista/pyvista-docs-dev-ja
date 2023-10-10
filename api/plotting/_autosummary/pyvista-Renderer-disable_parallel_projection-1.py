import pyvista as pv
from pyvista import demos
pl = pv.demos.orientation_plotter()
pl.disable_parallel_projection()
pl.show()
