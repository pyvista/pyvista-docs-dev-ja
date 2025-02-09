# Create a cylinder, translate it, and use iterative closest point to
# align mesh to its original position.
#
import pyvista as pv
import numpy as np
source = pv.Cylinder(resolution=30).triangulate().subdivide(1)
transformed = source.rotate_y(20).translate([-0.75, -0.5, 0.5])
aligned = transformed.align(source)
_, closest_points = aligned.find_closest_cell(
    source.points, return_closest_point=True
)
dist = np.linalg.norm(source.points - closest_points, axis=1)
#
# Visualize the source, transformed, and aligned meshes.
#
pl = pv.Plotter(shape=(1, 2))
_ = pl.add_text('Before Alignment')
_ = pl.add_mesh(source, style='wireframe', opacity=0.5, line_width=2)
_ = pl.add_mesh(transformed)
pl.subplot(0, 1)
_ = pl.add_text('After Alignment')
_ = pl.add_mesh(source, style='wireframe', opacity=0.5, line_width=2)
_ = pl.add_mesh(
    aligned,
    scalars=dist,
    scalar_bar_args={
        'title': 'Distance to Source',
        'fmt': '%.1E',
    },
)
pl.show()
#
# Show that the mean distance between the source and the target is
# nearly zero.
#
np.abs(dist).mean()  # doctest:+SKIP
# Expected:
## 9.997635192915073e-05
