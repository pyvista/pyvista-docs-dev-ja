from pyvista import examples
dataset = examples.download_cylinder_crossflow()
dataset.plot(cpos='xy', cmap='blues', rng=[-200, 500])
