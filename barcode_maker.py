#mark joseph
import turtle
from upc import*
# Screen object
wn = turtle.Screen()
wn.tracer(0)
turtle.hideturtle()
barcode_number = wn.textinput('barcode', 'Please enter a barcode')

def drawBars(barcode):
    bar = []
    # covert string to an integer array
    for ch in barcode:
        bar.append(int(ch))
    print(bar)



    turtle.setheading(90)

    x = -250# used to move the position and draw new squares
    for i in range(len(bar)):
        # if it is even it is a white bar otherwise it is blac
        if(i%2 == 0):
            turtle.pencolor("black")
        else:
            turtle.pencolor("white")
        # used for the unit size eg 1,2,3,4
        barcodeSize = bar[i]
        turtle.up()
        turtle.goto(x,0)
        turtle.down()
        turtle.pensize(barcodeSize*3)
        turtle.forward(300)
        x = x + 5

    wn.update()
    wn.mainloop()
#end of drawbars function



valid = True
while(valid):
    if(valid_barcode(barcode_number)):
            widths = generate_bar_widths(barcode_number)
            drawBars(widths)
            valid = False
    else:
            barcode_number = wn.textinput('barcode', 'Invalid Barcode\nPlease enter another barcode')
            print("NO")
print("done")


