from pyvista import examples
dataset = examples.download_moonlanding_image()
dataset.plot(
    cpos='xy',
    cmap='gray',
    background='w',
    show_scalar_bar=False,
)
