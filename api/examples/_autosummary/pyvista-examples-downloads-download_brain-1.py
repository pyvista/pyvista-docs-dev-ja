from pyvista import examples
dataset = examples.download_brain()
dataset.plot(volume=True)
#
# .. seealso::
#
#     :ref:`Brain Dataset <brain_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Brain Atlas With Sides Dataset <brain_atlas_with_sides_dataset>`
#
#     :ref:`medical_dataset_gallery`
#         Browse other medical datasets.
#
#     This dataset is used in the following examples:
#
#     * :ref:`gaussian_smoothing_example`
#     * :ref:`slice_example`
#     * :ref:`depth_peeling_example`
#     * :ref:`moving_isovalue_example`
