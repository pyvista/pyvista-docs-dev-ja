# Shows an interactive box that is used to resize and relocate a sphere.
#
import pyvista as pv
import numpy as np
plotter = pv.Plotter()
def simulate(widget):
    bounds = widget.bounds
    new_center = np.array(
        [
            (bounds[0] + bounds[1]) / 2,
            (bounds[2] + bounds[3]) / 2,
            (bounds[4] + bounds[5]) / 2,
        ]
    )
    new_radius = (
        min(
            (bounds[1] - bounds[0]) / 2,
            (bounds[3] - bounds[2]) / 2,
            (bounds[5] - bounds[4]) / 2,
        )
        - 0.3
    )
    sphere = pv.Sphere(new_radius, new_center)
    _ = plotter.add_mesh(sphere, name='Sphere')
_ = plotter.add_box_widget(callback=simulate)
plotter.show()
