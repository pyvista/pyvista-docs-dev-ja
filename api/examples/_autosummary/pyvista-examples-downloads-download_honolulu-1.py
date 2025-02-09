from pyvista import examples
dataset = examples.download_honolulu()
dataset.plot(
    scalars=dataset.points[:, 2],
    show_scalar_bar=False,
    cmap='gist_earth',
    clim=[-50, 800],
)
#
# .. seealso::
#
#     :ref:`Honolulu Dataset <honolulu_dataset>`
