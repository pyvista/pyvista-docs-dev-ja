# Generate protein ribbon.
#
import pyvista as pv
from pyvista import examples
tgqp = examples.download_3gqp()
ribbon = tgqp.protein_ribbon()
ribbon.plot()
