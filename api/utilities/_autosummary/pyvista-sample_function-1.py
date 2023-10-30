# Sample Perlin noise over a structured grid in 3D.
#
import pyvista as pv
noise = pv.perlin_noise(0.1, (1, 1, 1), (0, 0, 0))
grid = pv.sample_function(
    noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(60, 20, 20)
)
grid.plot(
    cmap='gist_earth_r', show_scalar_bar=False, show_edges=True
)
#
# Sample Perlin noise in 2D and plot it.
#
noise = pv.perlin_noise(0.1, (5, 5, 5), (0, 0, 0))
surf = pv.sample_function(noise, dim=(200, 200, 1))
surf.plot()
