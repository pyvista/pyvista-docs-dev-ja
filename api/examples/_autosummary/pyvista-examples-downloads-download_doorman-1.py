from pyvista import examples
dataset = examples.download_doorman()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Doorman Dataset <doorman_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`read_file_example`
