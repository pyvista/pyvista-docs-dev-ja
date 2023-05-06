from pyvista import examples
dataset = examples.download_kitchen()
dataset.streamlines(n_points=5).plot()
#
# This dataset is used in the following examples:
#
# * :ref:`plot_over_line_example`
