import pyvista as pv
prop = pv.Property(
    show_edges=True,
    color='brown',
    edge_color='blue',
    line_width=4,
    specular=1.0,
)
prop.plot()
