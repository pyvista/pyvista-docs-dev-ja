from pyvista import examples
import pyvista as pv
pl = pv.Plotter(lighting=None)
dataset = examples.download_cubemap_park()
_ = pl.add_actor(dataset.to_skybox())
pl.set_environment_texture(dataset, True)
pl.camera_position = 'xy'
pl.camera.zoom(0.4)
_ = pl.add_mesh(pv.Sphere(), pbr=True, roughness=0.1, metallic=0.5)
pl.show()
