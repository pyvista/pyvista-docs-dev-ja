import pyvista as pv
from pyvista import examples
vrml_file = examples.vrml.download_teapot()
pl = pv.Plotter()
pl.import_vrml(vrml_file)
pl.show()
