from pyvista import examples
dataset = examples.download_brain()
dataset.plot(volume=True)
#
# This dataset is used in the following examples:
#
# * :ref:`gaussian_smoothing_example`
# * :ref:`slice_example`
# * :ref:`depth_peeling_example`
# * :ref:`moving_isovalue_example`
