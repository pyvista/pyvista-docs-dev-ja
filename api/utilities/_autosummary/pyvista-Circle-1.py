import pyvista as pv
radius = 0.5
circle = pv.Circle(radius)
circle.plot(show_edges=True, line_width=5)
