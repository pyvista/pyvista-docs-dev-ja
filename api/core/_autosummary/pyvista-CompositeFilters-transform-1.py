# Translate a mesh by ``(50, 100, 200)``. Here a :class:`~pyvista.Transform` is
# used, but any :class:`~pyvista.TransformLike` is accepted.
#
import pyvista as pv
mesh = pv.MultiBlock([pv.Sphere(), pv.Plane()])
transform = pv.Transform().translate(50, 100, 200)
transformed = mesh.transform(transform, inplace=False)
transformed.plot(show_edges=True)
