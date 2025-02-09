# Add a camera3d widget to the scene.
#
import pyvista as pv
sphere = pv.Sphere()
plotter = pv.Plotter(shape=(1, 2))
_ = plotter.add_mesh(sphere, show_edges=True)
plotter.subplot(0, 1)
_ = plotter.add_mesh(sphere, show_edges=True)
_ = plotter.add_camera3d_widget()
plotter.show(cpos=plotter.camera_position)
