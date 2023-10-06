import pyvista
cylinder = pyvista.Cylinder(
    center=[1, 2, 3], direction=[1, 1, 1], radius=1, height=2
)
cylinder.plot(show_edges=True, line_width=5, cpos='xy')
#
pl = pyvista.Plotter()
_ = pl.add_mesh(
    pyvista.Cylinder(
        center=[1, 2, 3], direction=[1, 1, 1], radius=1, height=2
    ),
    show_edges=True,
    line_width=5,
)
pl.camera_position = "xy"
pl.show()
