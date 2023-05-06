from pyvista import examples
dataset = examples.download_office()
dataset.contour().plot()
#
# See :ref:`clip_with_plane_box_example` for an example using this
