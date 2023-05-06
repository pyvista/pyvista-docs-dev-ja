import pyvista as pv
prop = pv.Property()
prop.edge_color = 'red'
prop.edge_color
# Expected:
## Color(name='red', hex='#ff0000ff', opacity=255)
#
# Visualize red edges. Set the edge's visibility to ``True`` so we can see
# them.
#
prop.show_edges = True
prop.edge_color = 'red'
prop.plot()
