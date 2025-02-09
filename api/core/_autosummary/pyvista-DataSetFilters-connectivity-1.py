# Create a single mesh with three disconnected regions where each
# region has a different cell count.
#
import pyvista as pv
large = pv.Sphere(
    center=(-4, 0, 0), phi_resolution=40, theta_resolution=40
)
medium = pv.Sphere(
    center=(-2, 0, 0), phi_resolution=15, theta_resolution=15
)
small = pv.Sphere(center=(0, 0, 0), phi_resolution=7, theta_resolution=7)
mesh = large + medium + small
#
# Plot their connectivity.
#
conn = mesh.connectivity('all')
conn.plot(cmap=['red', 'green', 'blue'], show_edges=True)
#
# Restrict connectivity to a scalar range.
#
mesh['y_coordinates'] = mesh.points[:, 1]
conn = mesh.connectivity('all', scalar_range=[-1, 0])
conn.plot(cmap=['red', 'green', 'blue'], show_edges=True)
#
# Extract the region closest to the origin.
#
conn = mesh.connectivity('closest', (0, 0, 0))
conn.plot(color='blue', show_edges=True)
#
# Extract a region using a cell ID ``100`` as a seed.
#
conn = mesh.connectivity('cell_seed', 100)
conn.plot(color='green', show_edges=True)
#
# Extract the largest region.
#
conn = mesh.connectivity('largest')
conn.plot(color='red', show_edges=True)
#
# Extract the largest and smallest regions by specifying their
# region IDs. Note that the region IDs of the output differ from
# the specified IDs since the input has three regions but the output
# only has two.
#
large_id = 0  # largest always has ID '0'
small_id = 2  # smallest has ID 'N-1' with N=3 regions
conn = mesh.connectivity('specified', (small_id, large_id))
conn.plot(cmap=['red', 'blue'], show_edges=True)
