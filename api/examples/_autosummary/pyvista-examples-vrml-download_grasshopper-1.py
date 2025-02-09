import pyvista as pv
from pyvista import examples
vrml_file = examples.vrml.download_grasshopper()
pl = pv.Plotter()
pl.import_vrml(vrml_file)
pl.camera_position = [
    (25.0, 32.0, 44.0),
    (0.0, 0.931, -6.68),
    (-0.20, 0.90, -0.44),
]
pl.show()
