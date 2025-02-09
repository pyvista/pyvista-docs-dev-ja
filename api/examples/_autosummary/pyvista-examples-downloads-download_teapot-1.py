from pyvista import examples
dataset = examples.download_teapot()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Teapot Dataset <teapot_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`read_file_example`
