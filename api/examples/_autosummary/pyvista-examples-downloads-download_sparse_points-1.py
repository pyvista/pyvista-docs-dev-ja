from pyvista import examples
dataset = examples.download_sparse_points()
dataset.plot(scalars='val', render_points_as_spheres=True, point_size=50)
#
# .. seealso::
#
#     :ref:`Sparse Points Dataset <sparse_points_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`interpolate_example`
