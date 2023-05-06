from pyvista import examples
cpos = [
    [66.0, 73.0, -382.6],
    [66.0, 73.0, 0.0],
    [-0.0, -1.0, 0.0],
]
texture = examples.download_crater_imagery()
texture.plot(cpos=cpos)
