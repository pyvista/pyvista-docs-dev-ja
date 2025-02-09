from pyvista import examples
dataset = examples.download_moonlanding_image()
dataset.plot(
    cpos='xy',
    cmap='gray',
    background='w',
    show_scalar_bar=False,
)
#
# .. seealso::
#
#     :ref:`Moonlanding Image Dataset <moonlanding_image_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`image_fft_example`
