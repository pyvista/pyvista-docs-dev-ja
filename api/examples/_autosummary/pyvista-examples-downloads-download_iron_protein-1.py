from pyvista import examples
dataset = examples.download_iron_protein()
dataset.plot(volume=True, cmap='blues')
#
# .. seealso::
#
#     :ref:`Iron Protein Dataset <iron_protein_dataset>`
