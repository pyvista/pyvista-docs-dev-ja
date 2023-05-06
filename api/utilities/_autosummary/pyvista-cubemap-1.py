# Load a skybox given a directory, prefix, and file extension.
#
import pyvista
skybox = pyvista.cubemap(
    'my_directory', 'skybox', '.jpeg'
)  # doctest:+SKIP
