import pyvista as pv
chart = pv.Chart2D()
_ = chart.plot(range(10), range(10))
pl = pv.Plotter()
pl.add_chart(chart)
pl.show()
