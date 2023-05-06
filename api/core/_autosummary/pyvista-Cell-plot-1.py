from pyvista import examples
mesh = examples.load_hexbeam()
cell = mesh.get_cell(0)
cell.plot()
