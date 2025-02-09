# must have this here as our global backend may not be static
import pyvista
pyvista.set_jupyter_backend('static')
pyvista.global_theme.window_size = [600, 400]
pyvista.global_theme.anti_aliasing = 'fxaa'