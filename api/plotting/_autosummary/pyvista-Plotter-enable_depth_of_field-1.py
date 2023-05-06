# Create five spheres and demonstrate the effect of depth of field.
#
import pyvista as pv
from pyvista import examples
pl = pv.Plotter(lighting="three lights")
pl.background_color = "w"
for i in range(5):
    mesh = pv.Sphere(center=(-i * 4, 0, 0))
    color = [0, 255 - i * 20, 30 + i * 50]
    _ = pl.add_mesh(
        mesh,
        show_edges=False,
        pbr=True,
        metallic=1.0,
        color=color,
    )
pl.camera.zoom(1.8)
pl.camera_position = [
    (4.74, 0.959, 0.525),
    (0.363, 0.3116, 0.132),
    (-0.088, -0.0075, 0.996),
]
pl.enable_depth_of_field()
pl.show()
