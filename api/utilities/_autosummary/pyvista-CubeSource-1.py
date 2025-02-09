# Create a default CubeSource.
#
import pyvista as pv
source = pv.CubeSource()
source.output.plot(show_edges=True, line_width=5)
