from pyvista import examples
dataset = examples.download_thermal_probes()
dataset.plot(render_points_as_spheres=True, point_size=5, cpos='xy')
#
# .. seealso::
#
#     :ref:`Thermal Probes Dataset <thermal_probes_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`interpolate_example`
