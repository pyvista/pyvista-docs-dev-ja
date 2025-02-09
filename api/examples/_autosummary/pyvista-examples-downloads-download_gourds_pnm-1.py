from pyvista import examples
dataset = examples.download_gourds_pnm()
dataset.plot(rgba=True, cpos='xy')
#
# .. seealso::
#
#     :ref:`Gourds Pnm Dataset <gourds_pnm_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Gourds Dataset <gourds_dataset>`
