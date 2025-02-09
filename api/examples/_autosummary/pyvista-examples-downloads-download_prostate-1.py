from pyvista import examples
dataset = examples.download_prostate()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Prostate Dataset <prostate_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`medical_dataset_gallery`
