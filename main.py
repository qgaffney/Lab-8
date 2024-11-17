#Create Stack class
class Stack:
    #Define methods
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty.")

#Define is_balanced       
def is_balanced(expression):
    stack = []
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or \
               (char == '}' and top != '{') or \
               (char == ']' and top != '['):
                return False
            return not stack

#Test functions
print(is_balanced('(a+b)'))
print(is_balanced('[(a+b)-c]'))
print(is_balanced('{(a+b)*c}'))
print(is_balanced('(a+b'))
print(is_balanced('(a+b]})'))
print(is_balanced('({[a+b]})'))

#Define is_operator
def is_operator(char):
    return char in ['+', '-', '*', '/']

#Define precedence
def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

#Defien apply_op
def apply_op(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

#Define evaluate_expression
def evalaluate_expression(expression):
    values = []
    operators = []

    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i+= 1
            continue
        
        elif expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
            i -= 1

        elif expression[i] == '(':
            operators.append('(')

        elif expression[i] == ')':
            while operators[-1] != '(':
                values.append(apply_op(operators.pop(), values.pop(), values.pop()))
            operators.pop()

        else:
            while operators and precedence(operators[-1]) >= precedence(expression[i]):
                values.append(apply_op(operators.pop(), values.pop(), values.pop()))
            operators.append(expression[i])

        i += 1

#Test functions
result = 18 + 3 * 13 - 12 / 5
print(result)
result2 = 3 + (9 * 2) / 3 - 3
print(result2)
result3 = 18 / 3 * (3 + 3) - 1
print(result3)