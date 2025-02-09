import pyvista as pv
from pyvista import examples
dataset = examples.download_head()
pl = pv.Plotter()
_ = pl.add_volume(dataset, cmap='cool', opacity='sigmoid_6')
pl.camera_position = [
    (-228.0, -418.0, -158.0),
    (94.0, 122.0, 82.0),
    (-0.2, -0.3, 0.9),
]
pl.show()
#
# .. seealso::
#
#     :ref:`Head Dataset <head_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Head 2 Dataset <head_2_dataset>`
#
#     :ref:`medical_dataset_gallery`
#         Browse other medical datasets.
#
#     :ref:`volume_rendering_example`
