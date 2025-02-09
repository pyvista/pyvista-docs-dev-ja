from pyvista import examples
dataset = examples.download_antarctica_velocity()
dataset.plot(cpos='xy', clim=[1e-3, 1e4], cmap='Blues', log_scale=True)
#
# .. seealso::
#
#     :ref:`Antarctica Velocity Dataset <antarctica_velocity_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`antarctica_example`
