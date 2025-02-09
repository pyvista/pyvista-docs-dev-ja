# must have this here as our global backend may not be static
import pyvista
pyvista.set_plot_theme('document')
pyvista.set_jupyter_backend('static')
pyvista.global_theme.window_size = [600, 400]
pyvista.global_theme.axes.show = False
pyvista.global_theme.anti_aliasing = 'fxaa'
pyvista.global_theme.show_scalar_bar = False