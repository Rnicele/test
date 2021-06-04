from tkinter import *
from tkinter.ttk import *


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')
        self.root.resizable(False, False)
        self.equation = StringVar()
        self.total = ''
        self.irrigate()
        self.root.mainloop()

    def irrigate(self):
        Entry(
            self.root,
            textvariable=self.equation,
            font=('Segeo UI', 20, 'bold')
        ).grid(
            columnspan=5,
            ipady=18
        )

        buttons = [
            ['+', 1, 4, 1],
            ['-', 2, 4, 1],
            ['*', 3, 4, 1],
            ['/', 4, 4, 1],
            ['%', 1, 3, 1],
            ['+/-', 1, 2, 1],
            ['C', 1, 1, 1],
            ['.', 5, 1, 1],
            ['=', 5, 3, 2, 38],
            ['0', 5, 2, 1],
            ['1', 2, 1, 1],
            ['2', 2, 2, 1],
            ['3', 2, 3, 1],
            ['4', 3, 1, 1],
            ['5', 3, 2, 1],
            ['6', 3, 3, 1],
            ['7', 4, 1, 1],
            ['8', 4, 2, 1],
            ['9', 4, 3, 1],
        ]

        for button in buttons:
            self.make(*button)

    def make(self, label: str, row: int, column: int, column_span: int, ipadx=0):
        Button(
            self.root,
            text=label,
            command=lambda arg=label: self.evaluate(arg)
        ).grid(
            row=row,
            column=column,
            columnspan=column_span,
            ipadx=ipadx,
            ipady=15,
            sticky=W,
        )

    def evaluate(self, sign: str):
        if sign == 'C':
            self.equation.set('')
            return

        if (sign == '+/-'):
            return

        if (sign == '.') and ('.' in self.equation.get()):
            return

        if sign == '=':
            try:
                result = eval(self.equation.get())
                self.equation.set("{:.2f}".format(result))
            except SyntaxError:
                pass

            return

        self.equation.set(f"{self.equation.get()}{sign}")


Calculator()
