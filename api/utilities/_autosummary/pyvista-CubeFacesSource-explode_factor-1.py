import pyvista as pv
cube_faces_source = pv.CubeFacesSource(
    x_length=3, y_length=2, z_length=1, explode_factor=0.2
)
output = cube_faces_source.output
output.plot(show_edges=True, line_width=10)
#
# Note how all faces are moved by the same amount. Compare this to using
# :meth:`~pyvista.DataSetFilters.explode` where the distance each face moves
# is relative to distance of each face to the center of the cube.
#
exploded = pv.merge(output).explode(0.2)
exploded.plot(show_edges=True, line_width=10)
