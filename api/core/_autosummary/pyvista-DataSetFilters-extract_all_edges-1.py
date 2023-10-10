# Extract the edges of a sample unstructured grid and plot the edges.
# Note how it plots interior edges.
#
import pyvista as pv
from pyvista import examples
hex_beam = pv.read(examples.hexbeamfile)
edges = hex_beam.extract_all_edges()
edges.plot(line_width=5, color='k')
