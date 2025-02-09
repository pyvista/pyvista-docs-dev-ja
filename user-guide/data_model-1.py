import pyvista
pyvista.set_plot_theme('document')
pyvista.set_jupyter_backend('static')
points = [[.2, 0, 0], [1.3, 0, 0], [1, 1.2, 0], [0, 1, 0]]
cells = [4, 0, 1, 2, 3]
mesh = pyvista.PolyData(points, cells)

pl = pyvista.Plotter()
pl.add_mesh(mesh, show_edges=False)
pl.add_mesh(mesh.extract_feature_edges(), line_width=5, color='k')
pl.add_point_labels(mesh.points, [f'Point {i}' for i in range(4)], font_size=20, point_size=20)
pl.add_point_labels(mesh.center, ['Cell'], font_size=28)
pl.camera_position = 'xy'
pl.show()