# Create a ruled surface from a polyline.
#
import pyvista as pv
pl = pv.Plotter()
poly = pv.PolyData(
    [[0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 1, 1]],
    lines=[[2, 0, 1], [2, 2, 3]],
    force_float=False,
)
surface = poly.ruled_surface(resolution=(21, 21))
_ = pl.add_mesh(surface, show_edges=True)
pl.show()
