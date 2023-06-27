import pyvista as pv
from pyvista import examples
bunny = examples.download_bunny()
plotter = pv.Plotter()
_ = plotter.add_mesh(bunny, color='lightblue')
_ = plotter.add_silhouette(bunny, color='red', line_width=8.0)
plotter.view_xy()
plotter.show()
