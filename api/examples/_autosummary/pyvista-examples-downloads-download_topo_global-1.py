from pyvista import examples
dataset = examples.download_topo_global()
dataset.plot(cmap="gist_earth")
#
# This dataset is used in the following examples:
#
# * :ref:`surface_normal_example`
