# Take two different screenshots with two different window sizes.
#
import pyvista as pv
pl = pv.Plotter(off_screen=True)
_ = pl.add_mesh(pv.Cube())
with pl.window_size_context((400, 400)):
    pl.screenshot('/tmp/small_screenshot.png')  # doctest:+SKIP
with pl.window_size_context((1000, 1000)):
    pl.screenshot('/tmp/big_screenshot.png')  # doctest:+SKIP
