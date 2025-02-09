import pyvista as pv
from pyvista import examples
gltf_file = examples.gltf.download_damaged_helmet()
cubemap = examples.download_sky_box_cube_map()
pl = pv.Plotter()
pl.import_gltf(gltf_file)
pl.set_environment_texture(cubemap)
pl.show()
