# Catch VTK errors using the context manager.
#
import pyvista as pv
with pv.VtkErrorCatcher() as error_catcher:
    sphere = pv.Sphere()
