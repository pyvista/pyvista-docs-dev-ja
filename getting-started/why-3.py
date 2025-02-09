import pyvista
mesh = pyvista.Plane().triangulate()
submesh = mesh.subdivide(2, 'linear')
submesh.plot(show_edges=True)