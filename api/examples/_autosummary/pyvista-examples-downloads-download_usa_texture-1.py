import pyvista as pv
from pyvista import examples
dataset = examples.download_usa_texture()
dataset.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Usa Texture Dataset <usa_texture_dataset>`
#         See this dataset in the Dataset Gallery for more info.
