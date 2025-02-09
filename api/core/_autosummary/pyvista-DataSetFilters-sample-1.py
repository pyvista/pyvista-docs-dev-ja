# Resample data from another dataset onto a sphere.
#
import pyvista as pv
from pyvista import examples
mesh = pv.Sphere(center=(4.5, 4.5, 4.5), radius=4.5)
data_to_probe = examples.load_uniform()
result = mesh.sample(data_to_probe)
result.plot(scalars='Spatial Point Data')
#
# If sampling from a set of points represented by a ``(n, 3)``
# shaped ``numpy.ndarray``, they need to be converted to a
# PyVista DataSet, e.g. :class:`pyvista.PolyData`, first.
#
import numpy as np
points = np.array([[1.5, 5.0, 6.2], [6.7, 4.2, 8.0]])
mesh = pv.PolyData(points)
result = mesh.sample(data_to_probe)
result['Spatial Point Data']
# Expected:
## pyvista_ndarray([ 46.5 , 225.12])
