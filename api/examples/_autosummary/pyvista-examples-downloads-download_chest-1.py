from pyvista import examples
dataset = examples.download_chest()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Chest Dataset <chest_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`medical_dataset_gallery`
#         Browse other medical datasets.
#
#     :ref:`volume_rendering_example`
