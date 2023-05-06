from pyvista import examples
dataset = examples.download_doorman()
dataset.plot(cpos="xy")
#
# See :ref:`read_file_example` for an example using
