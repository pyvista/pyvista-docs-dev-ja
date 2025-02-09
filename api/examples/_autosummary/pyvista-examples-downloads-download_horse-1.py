from pyvista import examples
dataset = examples.download_horse()
dataset.plot(smooth_shading=True)
#
# .. seealso::
#
#     :ref:`Horse Dataset <horse_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Horse Points Dataset <horse_points_dataset>`
#
#     :ref:`disabling_mesh_lighting_example`
