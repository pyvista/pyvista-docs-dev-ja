import pyvista as pv
from pyvista import examples
gltf_file = examples.gltf.download_sheen_chair()
cubemap = examples.download_sky_box_cube_map()
pl = pv.Plotter()  # doctest:+SKIP
pl.import_gltf(gltf_file)  # doctest:+SKIP
pl.set_environment_texture(cubemap)  # doctest:+SKIP
pl.show()  # doctest:+SKIP
