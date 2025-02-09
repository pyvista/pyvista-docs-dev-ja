import pyvista as pv
from pyvista import examples
pl = pv.Plotter()
_ = pl.add_mesh(examples.load_hexbeam())
pl.export_vrml('sample')  # doctest:+SKIP
