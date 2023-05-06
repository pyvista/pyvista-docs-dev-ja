from pyvista import examples
dataset = examples.download_puppy_texture()
dataset.plot(cpos="xy")
#
# See :ref:`ref_texture_example` for an example using this
