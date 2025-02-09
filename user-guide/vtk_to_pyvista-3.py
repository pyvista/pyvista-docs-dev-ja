import pyvista

# create a default sphere and a shifted sphere
mesh_a = pyvista.Sphere()
mesh_b = pyvista.Sphere(center=(-0.4, 0, 0))
out, n_coll = mesh_a.collision(mesh_b, generate_scalars=True, contact_mode=2)

pl = pyvista.Plotter()
pl.add_mesh(out)
pl.add_mesh(mesh_b, style='wireframe', color='k')
pl.camera_position = 'xy'
pl.show()