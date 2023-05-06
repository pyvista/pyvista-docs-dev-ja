from pyvista import examples
dataset = examples.download_crater_topo()
dataset.plot(cmap="gist_earth", cpos="xy")
#
# This dataset is used in the following examples:
#
# * :ref:`terrain_following_mesh_example`
