from pyvista import examples
cpos = [
    [8.4287e02, -5.7418e02, -4.4085e02],
    [2.4950e02, 2.3450e02, 1.0125e02],
    [-3.2000e-01, 3.5000e-01, -8.8000e-01],
]
dataset = examples.download_frog()
dataset.plot(volume=True, cpos=cpos)
#
# See :ref:`volume_rendering_example` for an example using
