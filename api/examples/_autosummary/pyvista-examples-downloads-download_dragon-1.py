from pyvista import examples
dataset = examples.download_dragon()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Dragon Dataset <dragon_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`floors_example`
#     * :ref:`orbiting_example`
#     * :ref:`silhouette_example`
