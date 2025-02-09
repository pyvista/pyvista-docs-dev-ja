from pyvista import examples
dataset = examples.download_knee()
dataset.plot(cpos='xy', show_scalar_bar=False)
#
# .. seealso::
#
#     :ref:`Knee Dataset <knee_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Knee Full Dataset <knee_full_dataset>`
#
#     :ref:`medical_dataset_gallery`
#         Browse other medical datasets.
#
#     This dataset is used in the following examples:
#
#     * :ref:`plot_opacity_example`
#     * :ref:`volume_rendering_example`
