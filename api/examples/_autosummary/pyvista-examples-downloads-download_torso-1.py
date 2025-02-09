from pyvista import examples
dataset = examples.download_torso()
dataset.plot(cpos='xz')
#
# .. seealso::
#
#     :ref:`Torso Dataset <torso_dataset>`
