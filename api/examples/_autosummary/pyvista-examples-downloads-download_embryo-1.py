from pyvista import examples
dataset = examples.download_embryo()
dataset.plot(volume=True)
#
# This dataset is used in the following examples:
#
# * :ref:`contouring_example`
# * :ref:`resampling_example`
