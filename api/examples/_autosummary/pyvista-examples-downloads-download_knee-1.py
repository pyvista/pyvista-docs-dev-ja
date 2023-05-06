from pyvista import examples
dataset = examples.download_knee()
dataset.plot(cpos="xy", show_scalar_bar=False)
#
# This dataset is used in the following examples:
#
# * :ref:`plot_opacity_example`
# * :ref:`volume_rendering_example`
