# The following example generates a static image of the widget.
#
import pyvista as pv
mesh = pv.Sphere()
p = pv.Plotter()
actor = p.add_mesh(mesh)
def toggle_vis(flag):
    actor.SetVisibility(flag)
_ = p.add_checkbox_button_widget(toggle_vis, value=True)
p.show()
