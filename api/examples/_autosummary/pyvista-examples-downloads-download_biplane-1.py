from pyvista import examples
dataset = examples.download_biplane()
dataset.plot(cpos='zy', zoom=1.5)
#
# .. seealso::
#
#     :ref:`Biplane Dataset <biplane_dataset>`
