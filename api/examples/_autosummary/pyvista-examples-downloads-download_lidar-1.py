from pyvista import examples
dataset = examples.download_lidar()
dataset.plot(cmap="gist_earth")
#
# This dataset is used in the following examples:
#
# * :ref:`create_point_cloud`
