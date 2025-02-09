from pyvista import examples
dataset = examples.download_vtk()
dataset.plot(cpos='xy', line_width=5)
#
# .. seealso::
#
#     :ref:`Vtk Dataset <vtk_dataset>`
#         See this dataset in the Dataset Gallery for more info.
