import pyvista
from pyvista import examples
filename = examples.download_tecplot_ascii(load=False)
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh[0].plot()
