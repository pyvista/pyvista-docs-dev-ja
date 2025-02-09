# Extract a single value from a grid's point data.
#
import numpy as np
import pyvista as pv
from pyvista import examples
mesh = examples.load_uniform()
extracted = mesh.extract_values(0)
#
# Plot extracted values. Since adjacent cells are included by default, points with
# values other than ``0`` are included in the output.
#
extracted.get_data_range()
# Expected:
## (np.float64(0.0), np.float64(81.0))
extracted.plot()
#
# Set ``include_cells=False`` to only extract points. The output scalars now
# strictly contain zeros.
#
extracted = mesh.extract_values(0, include_cells=False)
extracted.get_data_range()
# Expected:
## (np.float64(0.0), np.float64(0.0))
extracted.plot(render_points_as_spheres=True, point_size=100)
#
# Use ``ranges`` to extract values from a grid's point data in range.
#
# Here, we use ``+/-`` infinity to extract all values of ``100`` or less.
#
extracted = mesh.extract_values(ranges=[-np.inf, 100])
extracted.plot()
#
# Extract every third cell value from cell data.
#
mesh = examples.load_hexbeam()
lower, upper = mesh.get_data_range()
step = 3
extracted = mesh.extract_values(
    range(lower, upper, step)  # values 0, 3, 6, ...
)
#
# Plot result and show an outline of the input for context.
#
pl = pv.Plotter()
_ = pl.add_mesh(extracted)
_ = pl.add_mesh(mesh.extract_all_edges())
pl.show()
#
# Any combination of values and ranges may be specified.
#
# E.g. extract a single value and two ranges, and split the result into separate
# blocks of a MultiBlock.
#
extracted = mesh.extract_values(
    values=18, ranges=[[0, 8], [29, 40]], split=True
)
extracted
# Expected:
## MultiBlock (...)
##   N Blocks:   3
##   X Bounds:   0.000e+00, 1.000e+00
##   Y Bounds:   0.000e+00, 1.000e+00
##   Z Bounds:   0.000e+00, 5.000e+00
extracted.plot(multi_colors=True)
#
# Extract values from multi-component scalars.
#
# First, create a point cloud with a 3-component RGB color array.
#
rng = np.random.default_rng(seed=1)
points = rng.random((30, 3))
colors = rng.random((30, 3))
point_cloud = pv.PointSet(points)
point_cloud['colors'] = colors
plot_kwargs = dict(render_points_as_spheres=True, point_size=50, rgb=True)
point_cloud.plot(**plot_kwargs)
#
# Extract values from a single component.
#
# E.g. extract points with a strong red component (i.e. > 0.8).
#
extracted = point_cloud.extract_values(ranges=[0.8, 1.0], component_mode=0)
extracted.plot(**plot_kwargs)
#
# Extract values from all components.
#
# E.g. extract points where all RGB components are dark (i.e. < 0.5).
#
extracted = point_cloud.extract_values(
    ranges=[0.0, 0.5], component_mode='all'
)
extracted.plot(**plot_kwargs)
#
# Extract specific multi-component values.
#
# E.g. round the scalars to create binary RGB components, and extract only green
# and blue components.
#
point_cloud['colors'] = np.round(point_cloud['colors'])
green = [0, 1, 0]
blue = [0, 0, 1]
extracted = point_cloud.extract_values(
    values=[blue, green],
    component_mode='multi',
)
extracted.plot(**plot_kwargs)
#
# Use the original IDs returned by the extraction to modify the original point
# cloud.
#
# For example, change the color of the blue and green points to yellow.
#
point_ids = extracted['vtkOriginalPointIds']
yellow = [1, 1, 0]
point_cloud['colors'][point_ids] = yellow
point_cloud.plot(**plot_kwargs)
