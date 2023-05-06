from pyvista import examples
dataset = examples.download_poly_line()
dataset.plot(line_width=5)
