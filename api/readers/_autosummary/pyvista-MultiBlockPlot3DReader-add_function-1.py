import pyvista
from pyvista import examples
filename = examples.download_file('multi-bin.xyz')
reader = pyvista.reader.MultiBlockPlot3DReader(filename)
reader.add_function(112)  # add a function by its integer value
reader.add_function(
    reader.PRESSURE_COEFFICIENT
)  # add a function by enumeration via class variable alias
