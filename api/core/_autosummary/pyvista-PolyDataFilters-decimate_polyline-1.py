# Generate a circle, builtin function returns a Polygon cell.
#
import pyvista as pv
circle = pv.Circle(resolution=30)
#
# Convert to a Polyline. A polyline requires duplicating reference
# to initial point to close the circle.
#
circle_polyline = pv.PolyData(
    circle.points, lines=[31] + list(range(30)) + [0]
)
circle_polyline.n_points
# Expected:
## 30
#
# Decimate ~50% of points.
#
decimate_some = circle_polyline.decimate_polyline(0.5)
decimate_some.n_points
# Expected:
## 14
#
# Decimate more points.
#
decimate_more = circle_polyline.decimate_polyline(0.75)
decimate_more.n_points
# Expected:
## 6
#
# Compare decimated polylines.
#
pl = pv.Plotter()
_ = pl.add_mesh(circle_polyline, label='Circle', color='red', line_width=5)
_ = pl.add_mesh(
    decimate_some,
    label='Decimated some',
    color='blue',
    line_width=5,
)
_ = pl.add_mesh(
    decimate_more,
    label='Decimated more',
    color='black',
    line_width=5,
)
pl.view_xy()
_ = pl.add_legend(face='line', size=(0.25, 0.25))
pl.show()
