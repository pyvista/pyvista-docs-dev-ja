import pyvista as pv
from pyvista import examples
dataset = examples.download_kitchen()
point_a = (0.08, 2.50, 0.71)
point_b = (0.08, 4.50, 0.71)
line = pv.Line(point_a, point_b, resolution=39)
streamlines = dataset.streamlines_from_source(line, max_length=200)
streamlines.plot(show_grid=True)
#
# .. seealso::
#
#     :ref:`Kitchen Dataset <kitchen_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`plot_over_line_example`
