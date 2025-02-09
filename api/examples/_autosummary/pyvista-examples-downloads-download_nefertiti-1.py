from pyvista import examples
dataset = examples.download_nefertiti()
dataset.plot(cpos='xz')
#
# .. seealso::
#
#     :ref:`Nefertiti Dataset <nefertiti_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`surface_normal_example`
#     * :ref:`extract_edges_example`
#     * :ref:`show_edges_example`
#     * :ref:`edl`
#     * :ref:`pbr_example`
