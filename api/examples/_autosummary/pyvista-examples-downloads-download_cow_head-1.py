from pyvista import examples
dataset = examples.download_cow_head()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Cow Head Dataset <cow_head_dataset>`
#         See this dataset in the Dataset Gallery for more info.
