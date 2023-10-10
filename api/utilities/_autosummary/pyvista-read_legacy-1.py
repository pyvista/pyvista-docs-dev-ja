# Load an example mesh using the legacy reader.
#
import pyvista as pv
from pyvista import examples
mesh = pv.read_legacy(examples.uniformfile)  # doctest:+SKIP
