# Sample a dataset along a high resolution circular arc and plot.
#
from pyvista import examples
mesh = examples.load_uniform()
a = [mesh.bounds.x_min, mesh.bounds.y_min, mesh.bounds.z_max]
b = [mesh.bounds.x_max, mesh.bounds.y_min, mesh.bounds.z_min]
center = [
    mesh.bounds.x_min,
    mesh.bounds.y_min,
    mesh.bounds.z_min,
]
mesh.plot_over_circular_arc(
    a, b, center, resolution=1000, show=False
)  # doctest:+SKIP
