from pyvista import examples
dataset = examples.download_vtk_logo()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Vtk Logo Dataset <vtk_logo_dataset>`
#         See this dataset in the Dataset Gallery for more info.
