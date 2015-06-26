from Istack import Stack

def mystr(anInteger):
    NumberStack = Stack()
    while anInteger >= 10:
        digit = anInteger % 10
        NumberStack.push(digit)
        anInteger = anInteger // 10
    NumberStack.push(anInteger)
    aString = ''
    for i in range(len(NumberStack)):
        aString = aString + chr(NumberStack.pop() + 48) 
    return aString

def evalPostfix( postfixExpression ):
    expressionlist = postfixExpression.split()
    expressionstack = Stack()
    for element in expressionlist:
        if element not in '+-*/':
            expressionstack.push(element)
        elif len(expressionstack) >= 2:
            num1 = float(expressionstack.pop())
            num2 = float(expressionstack.pop())
            num = ''
            if element == '+':
                num = num1 + num2
            elif element == '-':
                num = num2 - num1
            elif element == '*':
                num = num1 * num2
            elif element == '/':
                num = num2 / num1
            else:
                return None 
            if num != '':
                expressionstack.push(num)
            
    if len(expressionstack) == 1:
        return float(expressionstack.pop())
    
    
def evalPrefix( prefixExpression ):
    expressionlist = prefixExpression.split()
    expressionstack = Stack()   
    for element in expressionlist[::-1]:
        if element not in '+-*/':
            expressionstack.push(element)
        else:
            num1 = float(expressionstack.pop())
            num2 = float(expressionstack.pop())
            num = ''
            if element == '+':
                num = num1 + num2
            elif element == '-':
                num = num1 - num2
            elif element == '*':
                num = num1 * num2
            elif element == '/':
                num = num1 / num2
            else:
                return None    
            if num != '':
                expressionstack.push(num) 
                
    if len(expressionstack) == 1:
        return float(expressionstack.pop())
