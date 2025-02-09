from pyvista import examples
dataset = examples.download_embryo()
dataset.plot(volume=True)
#
# .. seealso::
#
#     :ref:`Embryo Dataset <embryo_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`medical_dataset_gallery`
#         Browse other medical datasets.
#
#     This dataset is used in the following examples:
#
#     * :ref:`contouring_example`
#     * :ref:`resampling_example`
