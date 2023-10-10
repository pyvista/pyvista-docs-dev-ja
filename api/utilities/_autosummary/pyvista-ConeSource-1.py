# Create a default ConeSource.
#
import pyvista as pv
source = pv.ConeSource()
source.output.plot(show_edges=True, line_width=5)
