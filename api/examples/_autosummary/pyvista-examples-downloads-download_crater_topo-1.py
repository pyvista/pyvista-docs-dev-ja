from pyvista import examples
dataset = examples.download_crater_topo()
dataset.plot(cmap='gist_earth', cpos='xy')
#
# .. seealso::
#
#     :ref:`Crater Topo Dataset <crater_topo_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`terrain_following_mesh_example`
