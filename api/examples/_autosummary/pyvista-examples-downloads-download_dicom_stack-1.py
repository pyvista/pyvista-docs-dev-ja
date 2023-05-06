from pyvista import examples
dataset = examples.download_dicom_stack()
dataset.plot(volume=True, zoom=3, show_scalar_bar=False)
