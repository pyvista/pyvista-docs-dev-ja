from pyvista import examples
dataset = examples.download_topo_land()
dataset.plot(clim=[-2000, 3000], cmap='gist_earth', show_scalar_bar=False)
#
# .. seealso::
#
#     :ref:`Topo Land Dataset <topo_land_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     This dataset is used in the following examples:
#
#     * :ref:`geodesic_example`
