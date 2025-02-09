# Create a disc with 50 points in the circumferential direction.
#
import pyvista as pv
source = pv.DiscSource(c_res=50)
source.output.plot(show_edges=True, line_width=5)
