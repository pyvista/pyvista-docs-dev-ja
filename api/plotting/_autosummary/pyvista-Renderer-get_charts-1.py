# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([1, 2, 3], [0, 1, 0])
pl = pv.Plotter()
pl.add_chart(chart)
chart is pl.renderer.get_charts()[0]
# Expected:
## True
