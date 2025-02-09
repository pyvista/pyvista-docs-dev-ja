import pyvista as pv
from pyvista import examples
#
filename = examples.download_m4_total_density(load=False)
reader = pv.get_reader(filename)
reader.hb_scale = 1.1
reader.b_scale = 10.0
#
grid = reader.read()
poly = reader.read(grid=False)
#
# Add the outline and volume to the plotter.
#
pl = pv.Plotter()
outline = pl.add_mesh(grid.outline(), color='black')
volume = pl.add_volume(grid)
#
# Add atoms and bonds to the plotter.
#
atoms = pl.add_mesh(poly.glyph(geom=pv.Sphere()), color='red')
bonds = pl.add_mesh(poly.tube(), color='white')
#
pl.show(cpos='zx')
#
# .. seealso::
#
#     :ref:`M4 Total Density Dataset <m4_total_density_dataset>`
