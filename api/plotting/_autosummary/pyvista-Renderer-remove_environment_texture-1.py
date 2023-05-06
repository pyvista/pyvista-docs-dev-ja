from pyvista import examples
import pyvista as pv
pl = pv.Plotter(lighting=None)
cubemap = examples.download_sky_box_cube_map()
_ = pl.add_mesh(
    pv.Sphere(), pbr=True, metallic=0.9, roughness=0.4
)
pl.set_environment_texture(cubemap)
pl.remove_environment_texture()
pl.camera_position = 'xy'
pl.show()
