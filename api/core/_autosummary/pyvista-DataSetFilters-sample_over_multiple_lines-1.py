# Sample over a plane that is interpolating a point cloud.
#
import pyvista as pv
import numpy as np
rng = np.random.default_rng(12)
point_cloud = rng.random((5, 3))
point_cloud[:, 2] = 0
point_cloud -= point_cloud.mean(0)
pdata = pv.PolyData(point_cloud)
pdata['values'] = rng.random(5)
plane = pv.Plane()
plane.clear_data()
plane = plane.interpolate(pdata, sharpness=3.5)
sample = plane.sample_over_multiple_lines(
    [[-0.5, -0.5, 0], [0.5, -0.5, 0], [0.5, 0.5, 0]]
)
pl = pv.Plotter()
_ = pl.add_mesh(pdata, render_points_as_spheres=True, point_size=50)
_ = pl.add_mesh(sample, scalars='values', line_width=10)
_ = pl.add_mesh(plane, scalars='values', style='wireframe')
pl.show()
