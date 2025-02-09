import pyvista as pv
cube_faces_source = pv.CubeFacesSource(
    x_length=3, y_length=2, z_length=1, shrink_factor=0.8
)
output = cube_faces_source.output
output.plot(show_edges=True, line_width=10)
#
# Note how all edges are shrunk by the same (constant) amount in terms of absolute
# distance. Compare this to :meth:`~pyvista.DataSetFilters.shrink` where the
# amount of shrinkage is relative to the size of the faces.
#
exploded = pv.merge(output).shrink(0.8)
exploded.plot(show_edges=True, line_width=10)
