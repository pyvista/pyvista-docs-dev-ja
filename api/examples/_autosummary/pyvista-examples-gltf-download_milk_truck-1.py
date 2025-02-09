import pyvista as pv
from pyvista import examples
gltf_file = examples.gltf.download_milk_truck()
pl = pv.Plotter()
pl.import_gltf(gltf_file)
pl.show()
