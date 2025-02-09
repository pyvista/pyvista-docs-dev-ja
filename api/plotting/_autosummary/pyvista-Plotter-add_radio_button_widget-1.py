# The following example creates a background color switcher.
#
import pyvista as pv
p = pv.Plotter()
def set_bg(color):
    def wrapped_callback():
        p.background_color = color

    return wrapped_callback
_ = p.add_radio_button_widget(
    set_bg('white'),
    'bgcolor',
    position=(10.0, 200.0),
    title='White',
    value=True,
)
_ = p.add_radio_button_widget(
    set_bg('lightblue'),
    'bgcolor',
    position=(10.0, 140.0),
    title='Light Blue',
)
_ = p.add_radio_button_widget(
    set_bg('pink'),
    'bgcolor',
    position=(10.0, 80.0),
    title='Pink',
)
p.show()
