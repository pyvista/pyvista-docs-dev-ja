# Download and plot the first frame of a simple GIF.
#
from pyvista import examples
grid = examples.download_gif_simple()
grid.plot(
    scalars='frame0',
    rgb=True,
    background='w',
    show_scalar_bar=False,
    cpos='xy',
)
#
# Plot the second frame.
#
grid.plot(
    scalars='frame1',
    rgb=True,
    background='w',
    show_scalar_bar=False,
    cpos='xy',
)
#
# .. seealso::
#
#     :ref:`Gif Simple Dataset <gif_simple_dataset>`
