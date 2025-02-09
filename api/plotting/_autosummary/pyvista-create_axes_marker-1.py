# Create the default axes marker.
#
import pyvista as pv
marker = pv.create_axes_marker()
pl = pv.Plotter()
_ = pl.add_actor(marker)
pl.show()
#
# Create an axes marker at the origin with custom colors and axis labels.
#
import pyvista as pv
marker = pv.create_axes_marker(
    line_width=4,
    ambient=0.0,
    x_color='#378df0',
    y_color='#ab2e5d',
    z_color='#f7fb9a',
    xlabel='X Axis',
    ylabel='Y Axis',
    zlabel='Z Axis',
    label_size=(0.1, 0.1),
)
pl = pv.Plotter()
_ = pl.add_actor(marker)
pl.show()
