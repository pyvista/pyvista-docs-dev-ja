from pyvista import examples
cpos = [
    [-2.3195e02, -3.3930e01, 1.2981e02],
    [-8.7100e00, 1.9000e-01, -1.1740e01],
    [-1.4000e-01, 9.9000e-01, 2.0000e-02],
]
dataset = examples.download_shark()
dataset.plot(cpos=cpos, smooth_shading=True)
