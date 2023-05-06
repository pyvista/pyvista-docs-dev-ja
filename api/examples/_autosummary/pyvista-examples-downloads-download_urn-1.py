from pyvista import examples
cpos = [
    [-7.123e02, 5.715e02, 8.601e02],
    [4.700e00, 2.705e02, -1.010e01],
    [2.000e-01, 1.000e00, -2.000e-01],
]
dataset = examples.download_urn()
dataset.plot(cpos=cpos)
