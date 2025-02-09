# Load a skybox given a directory, prefix, and file extension.
#
import pyvista as pv
skybox = pv.cubemap('my_directory', 'skybox', '.jpeg')  # doctest:+SKIP
