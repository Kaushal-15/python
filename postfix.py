def evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():
        if token.isdigit():  # If token is a number, push it to the stack
            stack.append(int(token))
        else:  # If token is an operator, pop two operands and apply the operation
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Integer division
            
    return stack.pop()

# Example usage
expression = "5 1 2 + 4 * + 3 -"  # Equivalent to: (5 + ((1 + 2) * 4)) - 3
result = evaluate_postfix(expression)
print("Result:", result)
