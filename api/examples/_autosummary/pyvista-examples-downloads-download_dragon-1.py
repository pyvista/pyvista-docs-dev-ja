from pyvista import examples
dataset = examples.download_dragon()
dataset.plot(cpos="xy")
#
# This dataset is used in the following examples:
#
# * :ref:`floors_example`
# * :ref:`orbiting_example`
# * :ref:`silhouette_example`
