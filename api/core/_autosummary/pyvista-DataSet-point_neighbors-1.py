# Get the point neighbors of the 0-th point.
#
import pyvista as pv
mesh = pv.Sphere(theta_resolution=10)
mesh.point_neighbors(0)
# Expected:
## [2, 226, 198, 170, 142, 114, 86, 254, 58, 30]
#
# Plot them.
#
pl = pv.Plotter()
_ = pl.add_mesh(mesh, show_edges=True)
_ = pl.add_point_labels(
    mesh.points[0], ["0"], text_color="blue", font_size=40
)
neighbors = mesh.point_neighbors(0)
_ = pl.add_point_labels(
    mesh.points[neighbors],
    labels=[f"{i}" for i in neighbors],
    text_color="red",
    font_size=40,
)
pl.camera_position = "yx"
pl.camera.zoom(7.0)
pl.show()
