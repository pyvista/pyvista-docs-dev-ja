# Open a MP4 movie and set the quality to maximum.
#
import pyvista as pv
pl = pv.Plotter()
pl.open_movie('movie.mp4', quality=10)  # doctest:+SKIP
