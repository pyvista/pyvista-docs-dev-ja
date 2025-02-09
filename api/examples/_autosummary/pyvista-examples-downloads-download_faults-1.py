from pyvista import examples
dataset = examples.download_faults()
dataset.plot(line_width=4)
#
# .. seealso::
#
#     :ref:`Faults Dataset <faults_dataset>`
