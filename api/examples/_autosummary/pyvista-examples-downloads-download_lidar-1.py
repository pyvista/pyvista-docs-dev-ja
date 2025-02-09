from pyvista import examples
dataset = examples.download_lidar()
dataset.plot(cmap='gist_earth')
#
# .. seealso::
#
#     :ref:`Lidar Dataset <lidar_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`create_point_cloud`
