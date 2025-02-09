import pyvista as pv
from pyvista import examples
filename = examples.download_particles(load=False)
reader = pv.get_reader(filename)
reader.reader.SetDataByteOrderToBigEndian()
reader.reader.Update()
mesh = reader.read()
mesh.plot()
#
# .. seealso::
#
#     :ref:`Particles Dataset <particles_dataset>`
