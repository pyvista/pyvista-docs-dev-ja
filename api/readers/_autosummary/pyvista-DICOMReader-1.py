# Read a DICOM stack.
#
import pyvista as pv
from pyvista import examples
path = examples.download_dicom_stack(load=False)
reader = pv.DICOMReader(path)
dataset = reader.read()
dataset.plot(volume=True, zoom=3, show_scalar_bar=False)
