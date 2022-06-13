# Add a skybox cubemap as an environment texture and show that the
# lighting from the texture is mapped on to a sphere dataset. Note how
# even when disabling the default lightkit, the scene lighting will still
# be mapped onto the actor.
#
from pyvista import examples
import pyvista as pv
pl = pv.Plotter(lighting=None)
cubemap = examples.download_sky_box_cube_map()
_ = pl.add_mesh(pv.Sphere(), pbr=True, metallic=0.9, roughness=0.4)
pl.set_environment_texture(cubemap)
pl.camera_position = 'xy'
pl.show()
