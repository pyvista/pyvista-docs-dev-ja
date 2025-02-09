from pyvista import examples
mesh = examples.download_dragon()
mesh['scalars'] = mesh.points[:, 1]
mesh.plot(cpos='xy', cmap='plasma')
