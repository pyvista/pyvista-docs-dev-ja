# Extract the edges from an unstructured grid.
#
import pyvista as pv
from pyvista import examples
hex_beam = pv.read(examples.hexbeamfile)
feat_edges = hex_beam.extract_feature_edges()
feat_edges.clear_data()  # clear array data for plotting
feat_edges.plot(line_width=10)
