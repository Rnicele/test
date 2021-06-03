from tkinter import * 
from tkinter.ttk import *
import tkinter.font as tkFont

root = Tk()
root.title('Calculator')
press_equation = ''


# input 
equation = StringVar()
equation_field= Entry(root, textvariable=equation)

# input widget
equation_field.grid(columnspan=5, ipadx=70)

press_equal = False

def pressnumber(num):
    global press_equation, press_equal

    if press_equal == False:
        press_equation = press_equation + str(num)
        equation.set(press_equation)
    else:
        total = total + str(num)
        equation.set(press_equation)

    # print(press_equation)


def pressreset(reset):
    print(reset)

def pressequal(equal):

    if  == False:
        press_equal = eval(press_equation)
        equation.set(press_equal)
        click_equals = True
    else:
        press_equal = eval(press_equation)
        equation.set(press_equal)
    print(total)

# operation button widget
addition = Button(root, text = "+", command=lambda: pressnumber('+'))
subtraction = Button(root, text = "-", command=lambda: pressnumber('-'))
multiplication = Button(root, text = "*", command=lambda: pressnumber('*'))
division = Button(root, text = "/", command=lambda: pressnumber('/'))
modulo = Button(root, text = "%", command=lambda: pressnumber('%'))
sign = Button(root, text = "+/-", command=lambda: pressnumber('+/-'))
reset = Button(root, text = "C", command=lambda: pressreset('reset'))
dot = Button(root, text = ".", command=lambda: pressnumber('.'))
equal = Button(root, text = "=", command=lambda: pressequal('='))

# number button widget
number1 = Button(root, text = "1", command=lambda: pressnumber(1))
number2 = Button(root, text = "2", command=lambda: pressnumber(2))
number3 = Button(root, text = "3", command=lambda: pressnumber(3))
number4 = Button(root, text = "4", command=lambda: pressnumber(4))
number5 = Button(root, text = "5", command=lambda: pressnumber(5))
number6 = Button(root, text = "6", command=lambda: pressnumber(6))
number7 = Button(root, text = "7", command=lambda: pressnumber(7))
number8 = Button(root, text = "8", command=lambda: pressnumber(8))
number9 = Button(root, text = "9", command=lambda: pressnumber(9))
number0 = Button(root, text = "0", command=lambda: pressnumber(0))

# arranging operation button widgets
reset.grid(row = 1, column = 1, sticky = E)
sign.grid(row = 1, column = 2, sticky = E)
modulo.grid(row = 1, column = 3, sticky = E)
addition.grid(row = 1, column = 4, sticky = E)
subtraction.grid(row = 2, column = 4, sticky = E)
multiplication.grid(row = 3, column = 4, sticky = E)
division.grid(row = 4, column = 4, sticky = E)
dot.grid(row = 5, column = 1, sticky = E)
equal.grid(row = 5, column = 3, columnspan=2, ipadx=38)

# arranging number button widgets
number1.grid(row = 2, column = 1, sticky = E)
number2.grid(row = 2, column = 2, sticky = E)
number3.grid(row = 2, column = 3, sticky = E)
number4.grid(row = 3, column = 1, sticky = E)
number5.grid(row = 3, column = 2, sticky = E)
number6.grid(row = 3, column = 3, sticky = E)
number7.grid(row = 4, column = 1, sticky = E)
number8.grid(row = 4, column = 2, sticky = E)
number9.grid(row = 4, column = 3, sticky = E)
number0.grid(row = 5, column = 2, sticky = E)

root.resizable(False, False) 
root.mainloop()