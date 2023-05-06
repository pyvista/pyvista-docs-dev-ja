# Clip a sphere by a plane and color the inside of the clipped sphere
# light blue using the ``backface_prop``.
#
import numpy as np
import pyvista as pv
plane = pv.Plane(i_size=1.5, j_size=1.5)
mesh = pv.Sphere().clip_surface(plane, invert=False)
pl = pv.Plotter()
actor = pl.add_mesh(mesh, smooth_shading=True)
actor.backface_prop.color = 'lightblue'
_ = pl.add_mesh(
    plane,
    opacity=0.25,
    show_edges=True,
    color='grey',
    lighting=False,
)
pl.show()
