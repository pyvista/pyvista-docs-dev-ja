import pyvista as pv
cube_faces_source = pv.CubeFacesSource(
    x_length=3, y_length=2, z_length=1, frame_width=0.2
)
cube_faces_source.output.plot(show_edges=True, line_width=10)
#
cube_faces_source.frame_width = 0.8
cube_faces_source.output.plot(show_edges=True, line_width=10)
