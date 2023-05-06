# Set the classic slider configuration.
#
import pyvista as pv
slider_styles = pv.global_theme.slider_styles
slider_styles.classic.slider_length = 0.02
slider_styles.classic.slider_width = 0.04
slider_styles.classic.slider_color = (0.5, 0.5, 0.5)
slider_styles.classic.tube_width = 0.005
slider_styles.classic.tube_color = (1.0, 1.0, 1.0)
slider_styles.classic.cap_opacity = 1
slider_styles.classic.cap_length = 0.01
slider_styles.classic.cap_width = 0.02
#
# Set the modern slider configuration.
#
slider_styles.modern.slider_length = 0.02
slider_styles.modern.slider_width = 0.04
slider_styles.modern.slider_color = (0.43, 0.44, 0.45)
slider_styles.modern.tube_width = 0.04
slider_styles.modern.tube_color = (0.69, 0.70, 0.709)
slider_styles.modern.cap_opacity = 0
slider_styles.modern.cap_length = 0.01
slider_styles.modern.cap_width = 0.02
