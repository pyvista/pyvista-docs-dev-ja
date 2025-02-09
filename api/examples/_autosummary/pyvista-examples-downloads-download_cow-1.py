from pyvista import examples
dataset = examples.download_cow()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Cow Dataset <cow_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Cow Head Dataset <cow_head_dataset>`
#
#     This dataset is used in the following examples:
#
#     * :ref:`extract_edges_example`
#     * :ref:`mesh_quality_example`
#     * :ref:`rotate_example`
#     * :ref:`linked_views_example`
