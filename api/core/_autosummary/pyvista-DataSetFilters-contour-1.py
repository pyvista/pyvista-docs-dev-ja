# Generate contours for the random hills dataset.
#
from pyvista import examples
hills = examples.load_random_hills()
contours = hills.contour()
contours.plot(line_width=5)
#
# Generate the surface of a mobius strip using flying edges.
#
import pyvista as pv
a = 0.4
b = 0.1
def f(x, y, z):
    xx = x * x
    yy = y * y
    zz = z * z
    xyz = x * y * z
    xx_yy = xx + yy
    a_xx = a * xx
    b_yy = b * yy
    return (
        (xx_yy + 1) * (a_xx + b_yy)
        + zz * (b * xx + a * yy)
        - 2 * (a - b) * xyz
        - a * b * xx_yy
    ) ** 2 - 4 * (xx + yy) * (a_xx + b_yy - xyz * (a - b)) ** 2
n = 100
x_min, y_min, z_min = -1.35, -1.7, -0.65
grid = pv.UniformGrid(
    dimensions=(n, n, n),
    spacing=(
        abs(x_min) / n * 2,
        abs(y_min) / n * 2,
        abs(z_min) / n * 2,
    ),
    origin=(x_min, y_min, z_min),
)
x, y, z = grid.points.T
values = f(x, y, z)
out = grid.contour(
    1,
    scalars=values,
    rng=[0, 0],
    method='flying_edges',
)
out.plot(color='tan', smooth_shading=True)
#
# See :ref:`common_filter_example` or
# :ref:`marching_cubes_example` for more examples using this
