# Demonstrate cleaning an UnstructuredGrid and show how it can be used to
# average the point data across merged points.
#
import pyvista as pv
from pyvista import examples
hexbeam = examples.load_hexbeam()
hexbeam_shifted = hexbeam.translate([1, 0, 0])
hexbeam.point_data['data'] = [0] * hexbeam.n_points
hexbeam_shifted.point_data['data'] = [1] * hexbeam.n_points
merged = hexbeam.merge(hexbeam_shifted, merge_points=False)
cleaned = merged.clean(average_point_data=True)
cleaned.n_points < merged.n_points
# Expected:
## True
#
# Show how point averaging using the ``clean`` method with
# ``average_point_data=True`` results in averaged point data for merged
# points.
#
pl = pv.Plotter(shape=(1, 2))
_ = pl.add_mesh(merged, scalars='data', show_scalar_bar=False)
pl.subplot(0, 1)
_ = pl.add_mesh(cleaned, scalars='data')
pl.show()
