class Calculator:
    def __init__(self):
        pass

    def add(self, x, y): 
        return print(f"Addition Result of {x} and {y} = {x + y}")
    
    def subtract(self, x, y):
        return print(f"Subtrction Result of {x} and {y} = {x - y}")
    
    def multiply(self, x, y):
        return print(f"Multiplication Result of {x} and {y} = {x * y}")
    
    def divide(self, x, y):
        if y == 0:
            return print("Cannot divide by Zero !!")
        else:
            return print(f"Division Result of {x} and {y} = {x / y}")
        
calculator1 = Calculator()        
        
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

Operation = input("___________Enter operation____________\n Enter(1,2,3 or 4)\n1.Addition\n2.Subtracton\n3.Multiplication\n4.Division.\n******************\n")
if Operation == "1":
    calculator1.add(num1,num2)
elif Operation == "2":
    calculator1.subtract(num1,num2)
elif Operation == "3":
    calculator1.multiply(num1,num2)
else :
    calculator1.divide(num1,num2)        

    
    
