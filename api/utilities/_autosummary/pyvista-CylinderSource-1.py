# Create a default CylinderSource.
#
import pyvista
source = pyvista.CylinderSource()
source.output.plot(show_edges=True, line_width=5)
