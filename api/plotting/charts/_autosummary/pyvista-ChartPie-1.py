# Create a pie plot showing the usage of tax money.
#
import pyvista
x = [128.3, 32.9, 31.8, 29.3, 21.2]
l = ["Social benefits", "Governance", "Economic policy", "Education", "Other"]
chart = pyvista.ChartPie(x, labels=l)
chart.show()
