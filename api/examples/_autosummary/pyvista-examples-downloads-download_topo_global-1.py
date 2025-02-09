from pyvista import examples
dataset = examples.download_topo_global()
dataset.plot(cmap='gist_earth')
#
# .. seealso::
#
#     :ref:`Topo Global Dataset <topo_global_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`surface_normal_example`
