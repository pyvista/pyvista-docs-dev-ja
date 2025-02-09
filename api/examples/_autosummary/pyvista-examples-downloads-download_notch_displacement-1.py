from pyvista import examples
dataset = examples.download_notch_displacement()
dataset.plot(cmap='bwr')
#
# .. seealso::
#
#     :ref:`Notch Displacement Dataset <notch_displacement_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Notch Stress Dataset <notch_stress_dataset>`
#
#     :ref:`Aero Bracket Dataset <aero_bracket_dataset>`
#
#     :ref:`Fea Bracket Dataset <fea_bracket_dataset>`
