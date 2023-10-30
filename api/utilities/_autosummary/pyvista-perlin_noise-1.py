# Create a Perlin noise function with an amplitude of 0.1, frequency
# for all axes of 1, and a phase of 0 for all axes.
#
import pyvista as pv
noise = pv.perlin_noise(0.1, (1, 1, 1), (0, 0, 0))
#
# Sample Perlin noise over a structured grid and plot it.
#
grid = pv.sample_function(noise, [0, 5, 0, 5, 0, 5])
grid.plot()
