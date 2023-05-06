from pyvista import examples
dataset = examples.download_knee_full()
cpos = [
    (-381.74, -46.02, 216.54),
    (74.8305, 89.2905, 100.0),
    (0.23, 0.072, 0.97),
]
dataset.plot(
    volume=True, cmap="bone", cpos=cpos, show_scalar_bar=False
)
#
# This dataset is used in the following examples:
#
# * :ref:`volume_rendering_example`
