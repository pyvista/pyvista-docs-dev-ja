import pyvista
from pyvista import examples
filename = examples.download_brain_atlas_with_sides(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'avg152T1_RL_nifti.nii.gz'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
