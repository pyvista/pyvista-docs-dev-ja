# Enable hidden line removal.
#
import pyvista as pv
#
# Load a cylinder which has cells with a wide spread
#
cyl = pv.Cylinder(direction=(0, 0, 1), height=2).elevation()
#
# Common display argument to make sure all else is constant
#
dargs = dict(
    scalars='Elevation', cmap='rainbow', show_edges=True
)
#
p = pv.Plotter(shape=(1, 2))
_ = p.add_mesh(
    cyl,
    interpolate_before_map=False,
    scalar_bar_args={'title': 'Elevation - interpolated'},
    **dargs
)
p.subplot(0, 1)
_ = p.add_mesh(
    cyl,
    interpolate_before_map=True,
    scalar_bar_args={'title': 'Elevation - interpolated'},
    **dargs
)
p.link_views()
p.camera_position = [
    (-1.67, -5.10, 2.06),
    (0.0, 0.0, 0.0),
    (0.00, 0.37, 0.93),
]
p.show()  # doctest: +SKIP
