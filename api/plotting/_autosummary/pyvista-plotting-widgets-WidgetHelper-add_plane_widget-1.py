# Shows an interactive plane moving along the x-axis in the random-hill example, which is used to mark the max altitude
# at a particular distance x.
#
import pyvista as pv
from pyvista import examples
mesh = examples.load_random_hills()
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
def callback(normal, origin):
    slc = mesh.slice(normal=normal, origin=origin)
    origin = list(origin)
    origin[2] = slc.bounds[5]
    peak_plane = pv.Plane(
        center=origin,
        direction=[0, 0, 1],
        i_size=20,
        j_size=20,
    )
    _ = pl.add_mesh(
        peak_plane, name="Peak", color='red', opacity=0.4
    )
_ = pl.add_plane_widget(callback, normal_rotation=False)
pl.show()
