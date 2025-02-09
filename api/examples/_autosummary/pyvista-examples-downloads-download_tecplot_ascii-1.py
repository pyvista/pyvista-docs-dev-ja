# Plot the example Tecplot dataset.
#
from pyvista import examples
import pyvista as pv
dataset = examples.download_tecplot_ascii()
dataset.plot()
#
# .. seealso::
#
#     :ref:`Tecplot Ascii Dataset <tecplot_ascii_dataset>`
