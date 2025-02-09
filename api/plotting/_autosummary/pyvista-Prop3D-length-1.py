import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
actor.length
# Expected:
## 1.7272069317100354
