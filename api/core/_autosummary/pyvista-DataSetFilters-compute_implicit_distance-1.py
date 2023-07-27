# Compute the distance between all the points on a sphere and a
# plane.
#
import pyvista as pv
sphere = pv.Sphere(radius=0.35)
plane = pv.Plane()
_ = sphere.compute_implicit_distance(plane, inplace=True)
dist = sphere['implicit_distance']
type(dist)
# Expected:
## <class 'pyvista.core.pyvista_ndarray.pyvista_ndarray'>
#
# Plot these distances as a heatmap. Note how distances above the
# plane are positive, and distances below the plane are negative.
#
pl = pv.Plotter()
_ = pl.add_mesh(
    sphere, scalars='implicit_distance', cmap='bwr'
)
_ = pl.add_mesh(plane, color='w', style='wireframe')
pl.show()
#
# We can also compute the distance from all the points on the
# plane to the sphere.
#
_ = plane.compute_implicit_distance(sphere, inplace=True)
#
# Again, we can plot these distances as a heatmap. Note how
# distances inside the sphere are negative and distances outside
# the sphere are positive.
#
pl = pv.Plotter()
_ = pl.add_mesh(
    plane,
    scalars='implicit_distance',
    cmap='bwr',
    clim=[-0.35, 0.35],
)
_ = pl.add_mesh(sphere, color='w', style='wireframe')
pl.show()
#
# See :ref:`clip_with_surface_example` and
# :ref:`voxelize_surface_mesh_example` for more examples using
