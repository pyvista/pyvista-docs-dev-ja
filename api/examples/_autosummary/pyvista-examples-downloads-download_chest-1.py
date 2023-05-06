from pyvista import examples
dataset = examples.download_chest()
dataset.plot(cpos="xy")
#
# See :ref:`volume_rendering_example` for an example using
