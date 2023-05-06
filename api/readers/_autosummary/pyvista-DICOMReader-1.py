# Read a DICOM stack.
#
import pyvista
from pyvista import examples
path = examples.download_dicom_stack(load=False)
reader = pyvista.DICOMReader(path)
dataset = reader.read()
dataset.plot(volume=True, zoom=3, show_scalar_bar=False)
