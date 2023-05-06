from pyvista import examples
cpos = [
    [4.66316700e04, 4.32796241e06, -3.82467050e05],
    [5.52532740e05, 3.98017300e06, -2.47450000e04],
    [4.10000000e-01, -2.90000000e-01, -8.60000000e-01],
]
dataset = examples.download_damavand_volcano()
dataset.plot(
    cpos=cpos, cmap="reds", show_scalar_bar=False, volume=True
)
