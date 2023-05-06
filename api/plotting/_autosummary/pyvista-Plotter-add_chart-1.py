import pyvista
chart = pyvista.Chart2D()
_ = chart.plot(range(10), range(10))
pl = pyvista.Plotter()
pl.add_chart(chart)
pl.show()
