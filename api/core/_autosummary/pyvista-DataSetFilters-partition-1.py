# Partition a simple UniformGrid into a :class:`pyvista.MultiBlock`
# containing each partition.
#
import pyvista as pv
grid = pv.UniformGrid(dimensions=(5, 5, 5))
out = grid.partition(4, as_composite=True)
out.plot(multi_colors=True, show_edges=True)
#
# Partition of the Stanford bunny.
#
from pyvista import examples
mesh = examples.download_bunny()
out = mesh.partition(4, as_composite=True)
out.plot(multi_colors=True, cpos='xy')
