import pyvista as pv
from pyvista import examples
filename = examples.download_particles(load=False)
reader = pv.get_reader(filename)
reader.endian = 'BigEndian'
filename.split('/')[-1]  # omit the path
# Expected:
## 'Particles.raw'
mesh = reader.read()
mesh.plot()
