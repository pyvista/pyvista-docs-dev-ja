from pyvista import examples
cpos = [
    [71.96, 86.1, 28.45],
    [3.5, 12.0, 1.0],
    [-0.18, -0.19, 0.96],
]
dataset = examples.download_blow()
dataset.plot(
    scalars='displacement1',
    component=1,
    cpos=cpos,
    show_scalar_bar=False,
    smooth_shading=True,
)
#
# .. seealso::
#
#     :ref:`Blow Dataset <blow_dataset>`
