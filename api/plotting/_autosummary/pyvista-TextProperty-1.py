# Create a text's property.
#
from pyvista import TextProperty
prop = TextProperty()
prop.opacity = 0.5
prop.background_color = "b"
prop.background_opacity = 0.5
prop.show_frame = True
prop.frame_color = "b"
prop.frame_width = 10
prop.frame_color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
