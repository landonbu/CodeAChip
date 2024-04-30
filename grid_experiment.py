import gdsfactory as gf
from gdsfactory.generic_tech import get_generic_pdk

# from open_pdks.sky130a import sky130a as sky

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

# @gf.cell
# def import_tile(gdspath):

@gf.cell
def start_tile(tile):

    c = gf.Component("tilestart?")

    ref1 = c.add_ref(tile)
    ref1.rotate(90)

    ref2 = c.add_ref(tile)
    ref2.rotate(180)

    return c;

# @gf.cell
def add_grid_member(toplevel, component, offset):
    # toplevel: the top level component to add to
    # component: the component being added
    # offset to add it

    toplevel.add_ref(component).move(offset)
    
    # return toplevel;

@gf.cell
def start_tile_pd(tilepath, xdim = 1, ydim = 1):

    c = gf.Component("tileimport")

    pd = gf.read.import_gds(tilepath)

    # add_grid_member(c, pd, [0, 0])

    for i in range(xdim):
        for j in range(ydim):
            add_grid_member(c, pd, [(pd.xsize + 20)*i, (pd.xsize + 20)*j])

    # c.add_ref(pd).move([-100, 0])

    # add_grid_member(c, pd, [10, 0])

    # add_grid_member(c, pd, [0, 20])
    
    return c;

# c = demo_polygons()
# g = start_tile(c)
g = start_tile_pd("./src_cells/just_the_pd.gds", xdim=10, ydim=20)
# g.plot()  # show it in KLayout
g.write_gds("./outfiles/test_out.gds")
g.show() # updates klive

# just run this .py file in a directory with access to gdsfactory and klayout