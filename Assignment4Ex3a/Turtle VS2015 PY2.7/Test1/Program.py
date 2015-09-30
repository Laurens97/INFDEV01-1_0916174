from Start import *

#For this assigment you are asked to use the drawing facilities of python provided by the turtle library.
#For simplicity we provide you an interface that hides the complexity of the turtle library.
#It is important for the correct execution of this program that you do not remove the header and the footer of
# this file.
#Add your code within the def Program(): ... (mind the spaces)
#
#If you try to run this sample a white screen will appear and a black triangle (from now on pen) will be drawn 
# in the middle.
#To move the pen we provide you two instructions: 
#   (i)    forward (amount)           'forward' moves the pen by 'amount' steps
#                                     amount is a value of type Integer
#
#   (ii)   turn (amount)              'turn' rotates the pen by 'amount' degrees
#                                     amount is a value of type Integer
#
#   (iii)  change_color_to (color)    'change_color_to' changes the color of the pen into 'color'
#                                      the possible colors are: Black, Green, Blue, and Red
#
#By combining forward and turn (inside loops) you are able to draw lots of nice shapes :) good luck and have fun!


def Program():
    #SUPPORTING INSTRUCTION
    #use 'get()' to read the input and store it into a variable. The input is provided in the shape of an ASCII integer number.
    #Check https://en.wikipedia.org/wiki/ASCII for the complete ASCII table 
    #Example:
    # The following code reads the input and stores it into a variable called 'x'. 'x' is then printed out into the console
    # x =get()
    # print (x)
    


    #---------------------------------------------------------------------
    #                  PUT YOUR CODE BELOW
    #---------------------------------------------------------------------
    change_color_to (Blue)

    x = get()

    if (x == int(ord("w")) or x == int(ord("W"))):
        forward(3)
    elif (x == int(ord("a")) or x == int(ord("A"))):
        turn (-45)
    elif (x == int(ord("d")) or x == int(ord("D"))):
        turn (45)
    elif (x == int(ord("s")) or x == int(ord("S"))):
        forward(-3)
    elif (x == int(ord("l")) or x == int(ord("L"))):
        turn(-180)
        forward(8)
        turn(90)
        forward(12)
        turn(90)
        forward(2)
        turn(90)
        forward(10)
        turn(-90)
        forward(6)
        turn(90)
        forward(2)
        turn(-180)
        forward(12)
        turn(90)
        forward(8)
        turn(90)
        forward(12)
        turn(90)
        forward(8)
        turn(180)
        forward(8)
        turn(-90)
        forward(12)
        turn(90)
        forward(2)
        turn(90)
        forward(10)
        turn(-90)
        forward(6)
        turn(90)
        forward(2)
        turn(90)
        forward(8)
    elif (x == int(ord("h")) or x == int(ord("H"))):
        print("Hi there. Thanks for playing this awesome game!")
        print("Move and rotate your cursor by pressing W, A, S or D.")
        print("Change your trail color to black, blue, red or green by pressing Z, B, R or G respectively.")
        print("Press L for a surprise!\n")
        print("You can exit by pressing X.\n\n")
    elif (x == int(ord("x")) or x == int(ord("X"))):
        exit()

run(Program)
from End import *
