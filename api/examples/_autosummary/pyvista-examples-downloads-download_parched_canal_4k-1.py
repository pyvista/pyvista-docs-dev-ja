from pyvista import examples
dataset = examples.download_parched_canal_4k()
dataset.plot(cpos="xy")
