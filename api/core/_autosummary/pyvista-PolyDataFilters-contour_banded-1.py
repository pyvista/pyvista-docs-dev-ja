# Plot the random hills dataset and with 8 contour lines. Note how we use 7
# colors here (``n_contours - 1``).
#
import pyvista as pv
from pyvista import examples
#
mesh = examples.load_random_hills()
n_contours = 8
_, edges = mesh.contour_banded(n_contours)
#
pl = pv.Plotter()
_ = pl.add_mesh(
    edges,
    line_width=5,
    render_lines_as_tubes=True,
    color='k',
)
_ = pl.add_mesh(mesh, n_colors=n_contours - 1, cmap='Set3')
pl.show()
#
# Extract the surface from the uniform grid dataset and plot its contours
# alongside the output from the banded contour filter.
#
surf = examples.load_uniform().extract_surface()
n_contours = 5
rng = [200, 500]
output, edges = surf.contour_banded(n_contours, rng=rng)
#
dargs = dict(n_colors=n_contours - 1, clim=rng)
pl = pv.Plotter()
_ = pl.add_mesh(
    edges,
    line_width=5,
    render_lines_as_tubes=True,
    color='k',
)
_ = pl.add_mesh(surf, opacity=0.3, **dargs)
_ = pl.add_mesh(output, **dargs)
pl.show()
