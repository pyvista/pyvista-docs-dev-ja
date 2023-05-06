from pyvista import examples
dataset = examples.download_teapot()
dataset.plot(cpos="xy")
#
# This dataset is used in the following examples:
#
# * :ref:`read_file_example`
