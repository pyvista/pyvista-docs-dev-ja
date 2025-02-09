# Load the dataset.
#
from pyvista import examples
dataset = examples.download_damavand_volcano()
#
# Use :meth:`~pyvista.ImageDataFilters.resample` to downsample it before plotting.
#
dataset = dataset.resample(0.5)
dataset.dimensions
# Expected:
## (140, 116, 85)
#
# Plot it.
#
cpos = [
    [4.66316700e04, 4.32796241e06, -3.82467050e05],
    [5.52532740e05, 3.98017300e06, -2.47450000e04],
    [4.10000000e-01, -2.90000000e-01, -8.60000000e-01],
]
dataset.plot(cpos=cpos, cmap='reds', show_scalar_bar=False, volume=True)
#
# .. seealso::
#
#     :ref:`Damavand Volcano Dataset <damavand_volcano_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`volume_rendering_example`
