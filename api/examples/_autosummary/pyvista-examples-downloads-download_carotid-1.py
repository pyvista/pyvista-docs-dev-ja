from pyvista import examples
cpos = [
    [220.96, -24.38, -69.96],
    [135.86, 106.55, 17.72],
    [-0.25, 0.42, -0.87],
]
dataset = examples.download_carotid()
dataset.plot(volume=True, cpos=cpos)
#
# This dataset is used in the following examples:
#
# * :ref:`glyph_example`
# * :ref:`gradients_example`
# * :ref:`streamlines_example`
