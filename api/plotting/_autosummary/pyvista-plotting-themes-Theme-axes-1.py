# Set the x axis color to black.
#
import pyvista as pv
pv.global_theme.axes.x_color = 'black'
#
# Show axes by default.
#
pv.global_theme.axes.show = True
#
# Use the ``vtk.vtkCubeAxesActor``.
#
pv.global_theme.axes.box = True
