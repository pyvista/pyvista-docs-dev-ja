# Download a point cloud. The points trace a path along topographical surface.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_gpr_path()
#
# Fit a line to the points and plot the result. The line of best fit is colored red.
#
line = pv.fit_line_to_points(mesh.points)
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='black', line_width=10)
_ = pl.add_mesh(line, color='red', line_width=5)
pl.show()
#
# Fit a line to a mesh and return the metadata.
#
mesh = examples.download_human()
line, length, direction = pv.fit_line_to_points(
    mesh.points, return_meta=True
)
#
# Show the length of the line.
#
length
# Expected:
## 167.6145387467733
#
# Plot the line as an arrow to show its direction.
#
arrow = pv.Arrow(
    start=line.points[0],
    direction=direction,
    scale=length,
    tip_length=0.2,
    tip_radius=0.04,
    shaft_radius=0.01,
)
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, opacity=0.5)
_ = pl.add_mesh(arrow, color='red')
pl.show()
#
# Set ``init_direction`` to the positive z-axis to flip the line's direction.
#
mesh = examples.download_human()
line, length, direction = pv.fit_line_to_points(
    mesh.points, init_direction='z', return_meta=True
)
#
# Plot the results again with an arrow.
#
arrow = pv.Arrow(
    start=line.points[0],
    direction=direction,
    scale=length,
    tip_length=0.2,
    tip_radius=0.04,
    shaft_radius=0.01,
)
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, opacity=0.5)
_ = pl.add_mesh(arrow, color='red')
pl.show()
