from pyvista import examples
dataset = examples.download_human()
dataset.plot(scalars='Color', rgb=True)
#
# .. seealso::
#
#     :ref:`Human Dataset <human_dataset>`
