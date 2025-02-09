import os
from tempfile import mkdtemp
import pyvista as pv
from pyvista import examples
filename = examples.download_dual_sphere_animation(load=False)
reader = pv.PVDReader(filename)
#
# Write the gif to a temporary directory. Normally you would write to a local
# path.
#
gif_filename = os.path.join(mkdtemp(), 'dual_sphere.gif')
#
# Generate the animation.
#
plotter = pv.Plotter()
plotter.open_gif(gif_filename)
for time_value in reader.time_values:
    reader.set_active_time_value(time_value)
    mesh = reader.read()
    _ = plotter.add_mesh(mesh, smooth_shading=True)
    _ = plotter.add_text(f'Time: {time_value:.0f}', color='black')
    plotter.write_frame()
    plotter.clear()
    plotter.enable_lightkit()
plotter.close()
#
# .. seealso::
#
#     :ref:`Dual Sphere Animation Dataset <dual_sphere_animation_dataset>`
#         See this dataset in the Dataset Gallery for more info.
