from pyvista import examples
dataset = examples.download_topo_land()
dataset.plot(
    clim=[-2000, 3000], cmap="gist_earth", show_scalar_bar=False
)
#
# This dataset is used in the following examples:
#
# * :ref:`geodesic_example`
