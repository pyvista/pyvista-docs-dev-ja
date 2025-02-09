from pyvista import examples
cpos = [(9.0, 1.0, 21.0), (-1.0, 2.0, -2.0), (0.0, 1.0, 0.0)]
dataset = examples.download_great_white_shark()
dataset.plot(cpos=cpos, smooth_shading=True)
#
# .. seealso::
#
#     :ref:`Great White Shark Dataset <great_white_shark_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Shark Dataset <shark_dataset>`
#         Similar dataset.
#
#     :ref:`Grey Nurse Shark Dataset <grey_nurse_shark_dataset>`
