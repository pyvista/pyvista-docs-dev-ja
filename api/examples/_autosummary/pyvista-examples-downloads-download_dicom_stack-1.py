from pyvista import examples
dataset = examples.download_dicom_stack()
dataset.plot(volume=True, zoom=3, show_scalar_bar=False)
#
# .. seealso::
#
#     :ref:`Dicom Stack Dataset <dicom_stack_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`medical_dataset_gallery`
