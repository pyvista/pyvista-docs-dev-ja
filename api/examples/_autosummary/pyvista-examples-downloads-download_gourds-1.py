from pyvista import examples
dataset = examples.download_gourds()
dataset.plot(rgba=True, cpos="xy")
#
# See :ref:`gaussian_smoothing_example` for an example using
