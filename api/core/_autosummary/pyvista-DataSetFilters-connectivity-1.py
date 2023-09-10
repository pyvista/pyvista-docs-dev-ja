# Label all connected regions.
#
# Load data.
#
import numpy as np
from pyvista import examples
import pyvista as pv
mesh = examples.download_foot_bones()
#
# Extract all disconnected regions.
#
conn = mesh.connectivity()
#
# Configure plotting parameters.
#
categories = True
cmap = 'glasbey'
#
# Format scalar bar text for integer values.
#
scalar_bar_args = dict(
    fmt='%.f',  # Do not show decimals
)
#
# Set the plot's camera position.
#
cpos = [(10.5, 12.2, 18.3), (0.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
#
# Plot the regions by ID.
#
# Note that region IDs are sorted in descending order by
# cell count.
#
conn.plot(
    categories=categories,
    cmap=cmap,
    scalar_bar_args=scalar_bar_args,
    cpos=cpos,
)
#
# Extract specific regions by size.
# Calculate region sizes.
#
# Get counts using the previous `connectivity('all')` results.
#
regions, region_sizes = np.unique(
    conn['RegionId'], return_counts=True
)
#
# Extract regions with fewer than 150 cells.
#
region_ids = regions[np.flatnonzero(region_sizes < 150)]
conn = mesh.connectivity('specified', region_ids)
#
# Plot result with plotting parameters defined earlier.
#
conn.plot(
    categories=categories,
    cmap=cmap,
    scalar_bar_args=scalar_bar_args,
    cpos=cpos,
)
#
# Extract the largest region.
#
conn = mesh.connectivity('largest', label_regions=False)
#
# Plot the largest region and show the input mesh for reference.
#
p = pv.Plotter()
_ = p.add_mesh(conn)
_ = p.add_mesh(mesh, style='wireframe')
p.show(cpos=cpos)
#
# Extract regions using seed points.
#
# Create hills and use curvature to define their peaks and valleys.
#
import pyvista as pv
mesh = pv.ParametricRandomHills()
mesh["Curvature"] = mesh.curvature()
#
# Visualize the peaks and valleys.
#
# Peaks have large positive curvature (i.e. are convex)
# Valleys have large negative curvature (i.e. are concave)
# Flat regions have curvature close to zero.
#
mesh.plot(
    clim=[-0.5, 0.5],
    cmap='bwr',
    below_color='blue',
    above_color='red',
)
#
# Extract the steepest peak using a seed point.
#
data_min, data_max = mesh.get_data_range()
peak_range = [0.2, data_max]  # Peak if curvature > 0.2
peak_point_id = np.argmax(mesh['Curvature'])  # Steepest point
peak_mesh = mesh.connectivity(
    'point_seed', peak_point_id, scalar_range=peak_range
)
#
# Extract the valley region closest to the steepest peak.
#
valley_range = [data_min, -0.2]  # Valley if curvature < 0.2
peak_point = mesh.points[peak_point_id]
valley_mesh = mesh.connectivity(
    'closest', peak_point, scalar_range=valley_range
)
#
# Plot extracted regions.
#
p = pv.Plotter()
_ = p.add_mesh(mesh, style='wireframe', color='lightgray')
_ = p.add_mesh(peak_mesh, color='red', label='Steepest Peak')
_ = p.add_mesh(
    valley_mesh, color='blue', label='Closest Valley'
)
_ = p.add_legend()
p.show()
