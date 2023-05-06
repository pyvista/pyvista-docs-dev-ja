from pyvista import examples
dataset = examples.download_brain_atlas_with_sides()
dataset.slice(normal='z').plot(cpos='xy')
