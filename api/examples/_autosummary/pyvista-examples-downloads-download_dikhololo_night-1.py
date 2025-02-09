import pyvista as pv
from pyvista import examples
gltf_file = examples.gltf.download_damaged_helmet()
texture = examples.download_dikhololo_night()
pl = pv.Plotter()
pl.import_gltf(gltf_file)
pl.set_environment_texture(texture)
pl.show()
#
# .. seealso::
#
#     :ref:`Dikhololo Night Dataset <dikhololo_night_dataset>`
