from pyvista import examples
dataset = examples.download_bunny()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Bunny Dataset <bunny_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Bunny Coarse Dataset <bunny_coarse_dataset>`
#
#     This dataset is used in the following examples:
#
#     * :ref:`read_file_example`
#     * :ref:`clip_with_surface_example`
#     * :ref:`extract_edges_example`
#     * :ref:`subdivide_example`
#     * :ref:`silhouette_example`
