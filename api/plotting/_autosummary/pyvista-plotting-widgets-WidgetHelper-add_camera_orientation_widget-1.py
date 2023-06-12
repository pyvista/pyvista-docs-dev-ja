# Add a camera orientation widget to the scene.
#
import pyvista
mesh = pyvista.Cube()
plotter = pyvista.Plotter()
_ = plotter.add_mesh(
    mesh, scalars=range(6), show_scalar_bar=False
)
_ = plotter.add_camera_orientation_widget()
plotter.show()
