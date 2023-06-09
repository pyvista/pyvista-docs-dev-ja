import pyvista as pv
sp0 = pv.Sphere()
sp1 = sp0.translate((1, 0, 0))
appended = sp0.append_polydata(sp1)
appended.plot()
#
# Append more than one PolyData.
#
sp2 = sp0.translate((-1, 0, 0))
appended = sp0.append_polydata(sp1, sp2)
appended.plot()
