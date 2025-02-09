# Sample a dataset over a circular arc and plot it.
#
import pyvista as pv
from pyvista import examples
uniform = examples.load_uniform()
uniform['height'] = uniform.points[:, 2]
pointa = [
    uniform.bounds.x_max,
    uniform.bounds.y_min,
    uniform.bounds.z_max,
]
pointb = [
    uniform.bounds.x_max,
    uniform.bounds.y_max,
    uniform.bounds.z_min,
]
center = [
    uniform.bounds.x_max,
    uniform.bounds.y_min,
    uniform.bounds.z_min,
]
sampled_arc = uniform.sample_over_circular_arc(pointa, pointb, center)
pl = pv.Plotter()
_ = pl.add_mesh(uniform, style='wireframe')
_ = pl.add_mesh(sampled_arc, line_width=10)
pl.show_axes()
pl.show()
