from pyvista import examples
dataset = examples.download_woman()
cpos = [
    (-2600.0, 1970.6, 1836.9),
    (48.5, -20.3, 843.9),
    (0.23, -0.168, 0.958),
]
dataset.plot(cpos=cpos)
#
# .. seealso::
#
#     :ref:`Woman Dataset <woman_dataset>`
