from pyvista import examples
dataset = examples.download_usa()
dataset.plot(style='wireframe', cpos='xy')
#
# .. seealso::
#
#     :ref:`Usa Dataset <usa_dataset>`
#         See this dataset in the Dataset Gallery for more info.
