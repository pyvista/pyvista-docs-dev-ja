import pyvista as pv
from pyvista import examples
gltf_file = examples.gltf.download_gearbox()
pl = pv.Plotter()
pl.import_gltf(gltf_file)
pl.show()
