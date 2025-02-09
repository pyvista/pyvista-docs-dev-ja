from pyvista import examples
dataset = examples.download_office()
dataset.contour().plot()
#
# .. seealso::
#
#     :ref:`Office Dataset <office_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`clip_with_plane_box_example`
