from pyvista import examples
dataset = examples.download_sparse_points()
dataset.plot(
    scalars="val", render_points_as_spheres=True, point_size=50
)
#
# See :ref:`interpolate_example` for an example using this
