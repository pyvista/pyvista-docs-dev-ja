# Output a simple point cloud represented as balls.
#
import numpy as np
import pyvista as pv
point_cloud = np.random.random((100, 3))
pdata = pv.PolyData(point_cloud)
pdata['orig_sphere'] = np.arange(100)
sphere = pv.Sphere(radius=0.02)
pc = pdata.glyph(scale=False, geom=sphere, orient=False)
pl = pv.Plotter()
_ = pl.add_mesh(
    pc,
    cmap='reds',
    smooth_shading=True,
    show_scalar_bar=False,
)
pl.export_gltf('balls.gltf')  # doctest:+SKIP
pl.show()
#
# Output the orientation plotter.
#
from pyvista import demos
pl = demos.orientation_plotter()
pl.export_gltf('orientation_plotter.gltf')  # doctest:+SKIP
pl.show()
