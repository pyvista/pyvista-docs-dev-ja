import pyvista as pv
from pyvista import examples
dataset = examples.download_head_2()
pl = pv.Plotter()
_ = pl.add_volume(dataset, cmap='cool', opacity='sigmoid_6')
pl.show()
#
# .. seealso::
#
#     :ref:`Head 2 Dataset <head_2_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Head Dataset <head_dataset>`
#
#     :ref:`medical_dataset_gallery`
