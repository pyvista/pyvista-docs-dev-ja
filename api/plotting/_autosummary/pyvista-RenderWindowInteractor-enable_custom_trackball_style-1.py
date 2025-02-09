# Create a simple scene with a plotter that has the left button
# dolly.
#
import pyvista as pv
plotter = pv.Plotter()
_ = plotter.add_mesh(pv.Cube(center=(1, 0, 0)))
_ = plotter.add_mesh(pv.Cube(center=(0, 1, 0)))
plotter.show_axes()
plotter.enable_custom_trackball_style(left='dolly')
plotter.show()  # doctest:+SKIP
