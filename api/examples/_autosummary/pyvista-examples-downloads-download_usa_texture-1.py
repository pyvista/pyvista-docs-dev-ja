import pyvista
from pyvista import examples
dataset = examples.download_usa_texture()
dataset.plot(cpos="xy")
