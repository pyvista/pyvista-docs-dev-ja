from pyvista import examples
cpos = [
    [ 4.66316700e+04,  4.32796241e+06, -3.82467050e+05],
    [ 5.52532740e+05,  3.98017300e+06, -2.47450000e+04],
    [ 4.10000000e-01, -2.90000000e-01, -8.60000000e-01]
]
dataset = examples.download_damavand_volcano()
dataset.plot(cpos=cpos, cmap="reds", show_scalar_bar=False, volume=True)
