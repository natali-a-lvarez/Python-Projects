user_input = input("Please enter an expression:  ") 

def calculator(expression):
    expression = expression.strip().split()
    x, operand, y = tuple(expression)

    x = int(x)
    y = int(y)
    
    if operand == 'x':
        return x * y
    elif operand == '/':
        return x / y
    elif operand == '-':
        return x - y
    elif operand == '+':
        return x + y
    else:
        return 'Please use a valid operand (+, -, x, /)'
        user_input = input("Please enter an expression") 
    
print("Your answer is: " + str(calculator(user_input)))