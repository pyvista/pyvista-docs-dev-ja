# Create an unstructured grid with both hexahedral and tetrahedral
# cells and then extract each individual cell type.
#
import pyvista as pv
from pyvista import examples
beam = examples.load_hexbeam()
beam = beam.translate([1, 0, 0])
ugrid = beam + examples.load_tetbeam()
hex_cells = ugrid.extract_cells_by_type(pv.CellType.HEXAHEDRON)
tet_cells = ugrid.extract_cells_by_type(pv.CellType.TETRA)
pl = pv.Plotter(shape=(1, 2))
_ = pl.add_text('Extracted Hexahedron cells')
_ = pl.add_mesh(hex_cells, show_edges=True)
pl.subplot(0, 1)
_ = pl.add_text('Extracted Tetrahedron cells')
_ = pl.add_mesh(tet_cells, show_edges=True)
pl.show()
