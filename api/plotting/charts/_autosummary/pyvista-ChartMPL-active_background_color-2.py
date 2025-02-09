import pyvista as pv
chart = pv.ChartMPL()
plots = chart.figure.axes[0].plot([0, 1, 2], [2, 1, 3])
chart.background_color = (0.5, 0.9, 0.5)
chart.show(interactive=False)
#
# Set the active background color to blue and activate the chart.
#
chart.active_background_color = 'b'
chart.show(interactive=True)
