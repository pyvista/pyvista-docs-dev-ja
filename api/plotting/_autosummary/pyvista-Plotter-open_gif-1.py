# Open a gif file, setting the framerate to 8 frames per second and
# reducing the colorspace to 64.
#
import pyvista as pv
pl = pv.Plotter()
pl.open_gif(
    'movie.gif', fps=8, palettesize=64
)  # doctest:+SKIP
