from pyvista import examples
dataset = examples.download_cylinder_crossflow()
dataset.plot(cpos='xy', cmap='blues', rng=[-200, 500])
#
# .. seealso::
#
#     :ref:`Cylinder Crossflow Dataset <cylinder_crossflow_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`2d_streamlines_example`
