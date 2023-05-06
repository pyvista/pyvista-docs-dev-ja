import pyvista
from pyvista import examples
gltf_file = examples.gltf.download_damaged_helmet()
texture = examples.download_dikhololo_night()
pl = pyvista.Plotter()
pl.import_gltf(gltf_file)
pl.set_environment_texture(texture)
pl.show()
