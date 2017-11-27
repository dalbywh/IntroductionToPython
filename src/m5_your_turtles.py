"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and William Dalby.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
fred_pen = 1
bob = rg.SimpleTurtle('turtle')
bob.pen = rg.Pen('midnight blue', 3)
bob.speed = 10

fred = rg.SimpleTurtle()
fred.pen = rg.Pen('green', fred_pen)
fred.speed = 10

size = 100

for k in range(10):
    # Put the pen down, then draw a square of the given size:

    bob.pen_up()
    bob.left(180)
    bob.forward(size)
    bob.pen_down()
    bob.draw_circle(size)

    bob.pen_up()
    bob.left(180)
    bob.forward(2 * size)
    bob.pen_down()
    bob.right(180)
    bob.draw_circle(size)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    bob.pen_down()
    size = size - 10

fred.pen_up()
fred.right(180)
fred.forward(600)
fred.left(90)
fred.forward(300)
fred.left(90)
fred.pen_down()
fred_size = 300
sides = 3
for q in range(10):
    fred.pen = rg.Pen('green', fred_pen)
    fred.draw_regular_polygon(sides, fred_size)
    fred_size = fred_size - 20
    sides = sides + 1
    fred_pen = fred_pen + 1
    fred.pen_up()
    fred.forward(10)
    fred.pen_down()

window.close_on_mouse_click()
