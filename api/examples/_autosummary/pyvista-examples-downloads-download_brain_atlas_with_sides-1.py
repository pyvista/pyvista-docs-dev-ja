from pyvista import examples
dataset = examples.download_brain_atlas_with_sides()
dataset.slice(normal='z').plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Brain Atlas With Sides Dataset <brain_atlas_with_sides_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Brain Dataset <brain_dataset>`
#
#     :ref:`medical_dataset_gallery`
