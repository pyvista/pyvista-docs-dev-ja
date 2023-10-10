# Determine which points on a plane are inside a manifold sphere
# surface mesh.  Extract these points using the
# :func:`DataSetFilters.extract_points` filter and then plot them.
#
import pyvista as pv
sphere = pv.Sphere()
plane = pv.Plane()
selected = plane.select_enclosed_points(sphere)
pts = plane.extract_points(
    selected['SelectedPoints'].view(bool),
    adjacent_cells=False,
)
pl = pv.Plotter()
_ = pl.add_mesh(sphere, style='wireframe')
_ = pl.add_points(pts, color='r')
pl.show()
