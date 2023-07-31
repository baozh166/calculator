class Calculator():
    def add(self, num1, num2):
        # return num1 + num2
        return 2
    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "error: denominator should not be 0"
        return num1/num2

if __name__ == "__main__":
    calculator = Calculator()
    print("add:", calculator.add(3, 1))
    print("sub:", calculator.subtract(3, 1))
    print("divide:", calculator.divide(3, 0))
    print("divide:", calculator.divide(3, 1))
