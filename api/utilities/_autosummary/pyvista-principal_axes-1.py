import pyvista as pv
import numpy as np
rng = np.random.default_rng(seed=0)  # only seeding for the example
#
# Create a mesh with points that have the largest variation in ``X``,
# followed by ``Y``, then ``Z``.
#
radii = np.array((6, 3, 1))  # x-y-z radii
mesh = pv.ParametricEllipsoid(
    xradius=radii[0], yradius=radii[1], zradius=radii[2]
)
#
# Plot the mesh and highlight its points in black.
#
p = pv.Plotter()
_ = p.add_mesh(mesh)
_ = p.add_points(mesh, color='black')
_ = p.show_grid()
p.show()
#
# Compute its principal axes and return the standard deviations.
#
axes, std = pv.principal_axes(mesh.points, return_std=True)
axes
# Expected:
## pyvista_ndarray([[-1.0000000e+00, -3.8287229e-08,  3.6589407e-10],
##                  [-3.8287229e-08,  1.0000000e+00, -3.0685656e-09],
##                  [-3.6589393e-10, -3.0685656e-09, -1.0000000e+00]],
##                 dtype=float32)
#
# Note that the principal axes have ones along the diagonal and zeros
# in the off-diagonal. This indicates that the first principal axis is
# aligned with the x-axis, the second with the y-axis, and third with
# the z-axis. This is expected, since the mesh is already axis-aligned.
#
# However, since the signs of the principal axes are arbitrary, the
# first and third axes in this case have a negative direction.
#
# Show the standard deviation along each axis.
#
std
# Expected:
## array([3.014956 , 1.507478 , 0.7035637], dtype=float32)
#
# Compare this to using :meth:`numpy.std` for the computation.
#
np.std(mesh.points, axis=0)
# Expected:
## pyvista_ndarray([3.0149572, 1.5074761, 0.7035699], dtype=float32)
#
# Since the points are axis-aligned, the two results agree in this case. In general,
# however, these two methods differ in that :meth:`numpy.std` with `axis=0` computes
# the standard deviation along the `x-y-z` axes, whereas the standard deviation
# returned by :meth:`principal_axes` is computed along the principal axes.
#
# Convert the values to proportions for analysis.
#
std / sum(std)
# Expected:
## array([0.5769149 , 0.28845742, 0.1346276 ], dtype=float32)
#
# From this result, we can determine that the axes explain approximately
# 58%, 29%, and 13% of the total variance in the points, respectively.
#
# Let's compare this to the proportions of the known radii of the ellipsoid.
#
radii / sum(radii)
# Expected:
## array([0.6, 0.3, 0.1])
#
# Note how the two ratios are similar, but do not match exactly. This is
# because the points of the ellipsoid are prolate and are denser near the
# poles. If the points were normally distributed, however, the proportions
# would match exactly.
#
# Create an array of normally distributed points scaled along the x-y-z axes.
# Use the same scaling as the radii of the ellipsoid from the previous example.
#
normal_points = rng.normal(size=(1000, 3))
scaled_points = normal_points * radii
axes, std = pv.principal_axes(scaled_points, return_std=True)
axes
# Expected:
## array([[-0.99997578,  0.00682346,  0.00136972],
##        [ 0.00681368,  0.99995213, -0.00702282],
##        [-0.00141757, -0.00701331, -0.9999744 ]])
#
# Once again, the axes have ones along the diagonal as expected since the
# points are already axis-aligned. Now let's examine the standard deviation
# and compare the relative proportions.
#
std
# Expected:
## array([5.94466738, 2.89590334, 1.02103169])
#
std / sum(std)
# Expected:
## array([0.60280948, 0.29365444, 0.10353608])
#
radii / sum(radii)
# Expected:
## array([0.6, 0.3, 0.1])
#
# Since the points are normally distributed, the relative proportion of
