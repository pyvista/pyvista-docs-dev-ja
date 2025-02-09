import pyvista as pv
from pyvista import examples
filename = examples.download_caffeine(load=False)
reader = pv.get_reader(filename)
poly = reader.read()
#
# Add atoms and bonds to the plotter.
#
pl = pv.Plotter()
atoms = pl.add_mesh(poly.glyph(geom=pv.Sphere(radius=0.1)), color='red')
bonds = pl.add_mesh(poly.tube(radius=0.1), color='gray')
pl.show(cpos='xy')
#
# .. seealso::
#
#     :ref:`Caffeine Dataset <caffeine_dataset>`
