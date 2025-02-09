from pyvista import examples
cpos = [
    [-200, -100, -16.0],
    [-20.0, 20.0, -2.00],
    [0.00, 0.00, 1.00],
]
dataset = examples.download_grey_nurse_shark()
dataset.plot(cpos=cpos, smooth_shading=True)
#
# .. seealso::
#
#     :ref:`Grey Nurse Shark Dataset <grey_nurse_shark_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Shark Dataset <shark_dataset>`
#         Similar dataset.
#
#     :ref:`Great White Shark Dataset <great_white_shark_dataset>`
