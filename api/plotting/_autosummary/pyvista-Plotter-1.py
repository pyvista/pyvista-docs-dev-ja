import pyvista as pv
mesh = pv.Cube()
another_mesh = pv.Sphere()
pl = pv.Plotter()
actor = pl.add_mesh(
    mesh, color='red', style='wireframe', line_width=4
)
actor = pl.add_mesh(another_mesh, color='blue')
pl.show()
