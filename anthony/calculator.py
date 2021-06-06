from tkinter import *
from tkinter.ttk import *


class Calculator:
    INITIAL_STATE = 'initial'
    EXPRESSION_STATE = 'expression'
    OPERATORS = ['+', '-', '*', 'x', '/', '÷', '%']
    BUTTONS = [
        ['+', 1, 4, 1],
        ['-', 2, 4, 1],
        ['x', 3, 4, 1],
        ['÷', 4, 4, 1],
        ['%', 1, 3, 1],
        ['+/-', 1, 2, 1],
        ['C', 1, 1, 1],
        ['.', 5, 1, 1],
        ['=', 5, 3, 2, 38],
        ['0', 5, 2, 1],
        ['7', 2, 1, 1],
        ['8', 2, 2, 1],
        ['9', 2, 3, 1],
        ['4', 3, 1, 1],
        ['5', 3, 2, 1],
        ['6', 3, 3, 1],
        ['1', 4, 1, 1],
        ['2', 4, 2, 1],
        ['3', 4, 3, 1],
    ]

    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')
        self.root.resizable(False, False)
        self.state = self.INITIAL_STATE
        self.equation = StringVar()
        self.result = ''
        self.operator = ''
        self.expression = ''
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

        for button in self.BUTTONS:
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
            self.reset()
            return

        if sign == '=':
            self.calculate()
            return

        if self.state == self.INITIAL_STATE:
            if sign in self.OPERATORS:
                if self.result == '':
                    return

                self.set_to_expression_state(sign)
                return

            if (sign == '.') and ('.' in self.result):
                return

            if sign == '+/-':
                if self.result == '':
                    return

                self.result = str(self.prune_zero(float(self.result) * -1))
                self.equation.set(self.result)
                return

            self.result = f"{self.result}{sign}"
            self.equation.set(self.result)

        if self.state == self.EXPRESSION_STATE:
            if sign in self.OPERATORS:
                self.calculate()
                self.set_to_expression_state(sign)
                return

            if (sign == '.') and ('.' in self.expression):
                return

            if sign == '+/-':
                if self.expression == '':
                    return

                self.expression = str(self.prune_zero(
                    float(self.expression) * -1))
                self.equation.set(
                    f"{self.result}{self.operator}{self.expression}")
                return

            self.expression = f"{self.expression}{sign}"
            self.equation.set(f"{self.result}{self.operator}{self.expression}")

    def calculate(self):
        try:
            self.operator = self.operator.replace('x', '*').replace('÷', '/')
            result = eval(f"{self.result}{self.operator}{self.expression}")
            self.result = self.prune_zero(result)
            self.equation.set(self.result)
            self.state = self.INITIAL_STATE
            self.operator = ''
            self.expression = ''
        except (SyntaxError, ZeroDivisionError):
            pass

    def prune_zero(self, expression: str):
        return expression if expression % 1 != 0 else int(expression)

    def set_to_expression_state(self, sign):
        self.operator = sign
        self.equation.set(f"{self.result}{self.operator}")
        self.state = self.EXPRESSION_STATE

    def reset(self):
        self.state = self.INITIAL_STATE
        self.equation.set('')
        self.result = ''
        self.operator = ''
        self.expression = ''


Calculator()
