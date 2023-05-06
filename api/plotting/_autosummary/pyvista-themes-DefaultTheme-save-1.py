# Export and then load back in a theme.
#
import pyvista as pv
theme = pv.themes.DefaultTheme()
theme.background = 'white'
theme.save('my_theme.json')  # doctest:+SKIP
loaded_theme = pv.load_theme('my_theme.json')  # doctest:+SKIP
