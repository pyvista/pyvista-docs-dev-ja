import pyvista as pv
from pyvista import examples
dataset = examples.download_bolt_nut()
pl = pv.Plotter()
_ = pl.add_volume(
    dataset,
    cmap='coolwarm',
    opacity='sigmoid_5',
    show_scalar_bar=False,
)
pl.camera_position = [
    (194.6, -141.8, 182.0),
    (34.5, 61.0, 32.5),
    (-0.229, 0.45, 0.86),
]
pl.show()
#
# .. seealso::
#
#     :ref:`Bolt Nut Dataset <bolt_nut_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`volume_rendering_example`
