import pyvista as pv
from pyvista import examples
gltf_file = examples.gltf.download_avocado()
pl = pv.Plotter()
pl.import_gltf(gltf_file)
pl.show()
