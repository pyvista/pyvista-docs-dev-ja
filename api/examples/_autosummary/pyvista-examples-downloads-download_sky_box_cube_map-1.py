from pyvista import examples
import pyvista as pv
pl = pv.Plotter()
dataset = examples.download_sky_box_cube_map()
_ = pl.add_actor(dataset.to_skybox())
pl.set_environment_texture(dataset)
pl.show()
