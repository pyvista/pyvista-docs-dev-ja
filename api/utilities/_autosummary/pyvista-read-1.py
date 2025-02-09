# Load an example mesh.
#
import pyvista as pv
from pyvista import examples
mesh = pv.read(examples.antfile)
mesh.plot(cpos='xz')
#
# Load a vtk file.
#
mesh = pv.read('my_mesh.vtk')  # doctest:+SKIP
#
# Load a meshio file.
#
mesh = pv.read('mesh.obj')  # doctest:+SKIP
#
# Load a pickled mesh file.
#
mesh = pv.read('mesh.pkl')  # doctest:+SKIP
