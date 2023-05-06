# First, create sample data to smooth. Here, we use
# :func:`pyvista.perlin_noise() <pyvista.utilities.common.perlin_noise>`
# to create meaningful data.
#
import numpy as np
import pyvista
noise = pyvista.perlin_noise(0.1, (2, 5, 8), (0, 0, 0))
grid = pyvista.sample_function(
    noise, [0, 1, 0, 1, 0, 1], dim=(20, 20, 20)
)
grid.plot(show_scalar_bar=False)
#
# Next, smooth the sample data.
#
smoothed = grid.median_smooth(kernel_size=(10, 10, 10))
smoothed.plot(show_scalar_bar=False)
