##### START:: CALCULATOR 1 ###################
### SIMPLE CALCULATOR

class Calculator:
    def run(self):
        checkEQ = False
        while checkEQ == False:
            try:
                equation = input('Equation: ')
                total = eval(equation)
                print(total)
                checkEQ = True
            except NameError: #if true tooo
                checkEQ = False

        print(checkEQ)
        self.total = total
        self.again()
        

    def again(self):
        confirm = input('Do you want to continue? (y/n): ')
        while confirm == 'y':
            op1 = input('please choose math operation (+, -, *, /, %): ')
            oper = self.checkOp(op1)

            while oper == False:
                op1 = input('please choose math operation (+, -, *, /, %): ')
                oper = self.checkOp(op1)
            else:
                checkEQ = False
                while checkEQ == False:
                    try:
                        new_eval = input('New equation: ')
                        new_total = eval(new_eval)
                        checkEQ = True
                    except NameError: 
                        checkEQ = False

                final_total = eval(f"{self.total}{op1}{new_total}")
                self.total = final_total

                print(self.total)
                confirm = input('Do you want to continue? (y/n): ')

        else:
            print('calcu exit')

    def checkOp(self, op):
        print(op)
        operator = ['+', '-', '*', '/', '%']
        return op in operator


calcu = Calculator()
calcu.run()
##### END:: CALCULATOR 1 #####################
