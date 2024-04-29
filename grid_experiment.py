import gdsfactory as gf
from gdsfactory.generic_tech import get_generic_pdk

gf.config.rich_output()
gf.CONF.display_type = "klayout"

PDK = get_generic_pdk()
PDK.activate()


@gf.cell
def demo_polygons():
    # Create a blank component (essentially an empty GDS cell with some special features)
    c = gf.Component()

    # Create and add a polygon from separate lists of x points and y points
    # (Can also be added like [(x1,y1), (x2,y2), (x3,y3), ... ]
    poly1 = c.add_polygon(
        [(-8, -6, -7, -9), (-6, 8, 17, 5)], layer=(1, 0)
    )  # GDS layers are tuples of ints (but if we use only one number it assumes the other number is 0)
    return c


c = demo_polygons()
c.plot()  # show it in KLayout