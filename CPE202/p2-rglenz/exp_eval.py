from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    stack=Stack(30)
    #create a list of the input string so the values are easier to manipulate
    strlst=input_str.split()
    oplst=['+','-','/','*','**','<<','>>']
    #this try except will catch if there aren't enough operands to complete the calcualtion
    try:
        #these tests will be run for every single value in the strlist
        for item in strlst:
            #determine if the item in the expression is invalid
            if item not in oplst:
                try:
                    item=int(item)
                        
                except(Exception):
                    try:
                        item=float(item)
                    except:
                        raise PostfixFormatException("Invalid token")
            #handles when an operator is encountered 
            if item == '+':
                op1=stack.pop()
                op2=stack.pop()
                stack.push(op2+op1)
            elif item == '-':
                op1=stack.pop()
                op2=stack.pop()
                stack.push(op2-op1)
            elif item == '*':
                op1=stack.pop()
                op2=stack.pop()
                stack.push(op1*op2)
            elif item == '/':
                op1=stack.pop()
                op2=stack.pop()
                if op1 == 0:
                    raise ValueError
                stack.push(op2/op1)
            elif item == '**':
                op1=stack.pop()
                op2=stack.pop()
                stack.push(op2**op1)
            elif item == '<<':
                op1=stack.pop()
                op2=stack.pop()
                stack.push(bitwise_shift(op2,op1,"<<"))
            elif item == '>>':
                op1=stack.pop()
                op2=stack.pop()
                stack.push(bitwise_shift(op2,op1,">>"))
            else:
            #if it is not an operator we push it onto the stack
                stack.push(item)
    except IndexError:
        raise PostfixFormatException('Insufficient operands')
    exp=stack.pop()
    #this ensures there werent enough operands. If there were there would still be something on the stack
    try:
        stack.peek()
    except IndexError:
        return exp
    raise PostfixFormatException('Too many operands')

def bitwise_shift(item,num,op):
    '''Calculates and returns the bitwise shift if the operator occurs. The arguments taken
    in are the two operands and the operator either left or right.'''
    if op=='<<':
        if item<=0:
            raise PostfixFormatException('Illegal bit shift operand')
        elif type(item)==float:
            raise PostfixFormatException('Illegal bit shift operand')
        elif type(num)==float:
            raise PostfixFormatException('Illegal bit shift operand')
        return item*(2**num)
    if op=='>>':
        if item<=0:
            raise PostfixFormatException('Illegal bit shift operand')
        elif type(item)==float:
            raise PostfixFormatException('Illegal bit shift operand')
        elif type(num)==float:
            raise PostfixFormatException('Illegal bit shift operand')
        return item//(2**num)
    


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    stack=Stack(30)
    strlst=input_str.split()
    exp=''
    oplst=['+','-','/','*','**','<<','>>']
    for item in strlst:  
        #detemine if the item is an integer if not keep going    
        try:
            int(item)
            exp+=item+' '
        except:
            try:
                float(item)
                exp+=item+' '
            except(Exception):
                None
        #handles parentheses
        if item=='(':
            stack.push(item)
        elif item==')':
            nitem=stack.pop()
            if nitem != '(':
                exp+=nitem+' '
            while stack.is_empty()!= True and nitem != "(":
                nitem=stack.pop()
                if nitem != '(':
                    exp+=nitem+' '    
        #handles operators 
        elif item in oplst:
            if stack.is_empty()!=True:
                o2=stack.peek()
                while o2 in oplst:
                    #handles precedence using helper function
                    op1, prec1=infix_to_postfix_prec(item)
                    op2, prec2=infix_to_postfix_prec(stack.peek())
                    if op1 == '**':
                        if prec1<prec2:
                            nitem=stack.pop()
                            exp+=nitem+' '
                            if stack.is_empty()!=True:
                                o2=stack.peek()
                            else:
                                o2=1
                        elif prec1 >= prec2:
                            break  
                    elif op1 != '**':
                        if prec1<=prec2:
                            nitem=stack.pop()
                            exp+=nitem+' '
                            if stack.is_empty()!=True:
                                o2=stack.peek()
                            else:
                                o2=1
                        elif prec1 > prec2:
                            break       
            stack.push(item)
    #adds the remaining items in the stack to the expression
    while stack.is_empty()==False:
        nitem=stack.pop()
        exp+=nitem+' '
    #returns the expression minus the space at the end 
    return(exp[:-1])

def infix_to_postfix_prec(item):
    """Calculates an operators precedence by taking in the operator
    and returning its corresponding value and the operator to be manipulated."""
    prec=0
    if item=="+":
        prec=0
    if item=="-":
        prec=0
    if item=="*":
        prec=1
    if item=="/":
        prec=1
    if item=="**":
        prec=2
    if item=="<<":
        prec=3
    if item==">>":
        prec=3
    return item,prec

def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack=Stack(30)
    exp=''
    strlst=input_str.split()
    #reads the expression backwards 
    for i in range (len(strlst)-1,-1,-1):
        #handles operators 
        if strlst[i] == '+':
            op1=stack.pop()
            op2=stack.pop()
            stack.push(op1+' '+op2+' +')
        elif strlst[i] == '-':
            op1=stack.pop()
            op2=stack.pop()
            stack.push(op1+' '+op2+' -')
        elif strlst[i] == '*':
            op1=stack.pop()
            op2=stack.pop()
            stack.push(op1+' '+op2+' *')
        elif strlst[i] == '/':
            op1=stack.pop()
            op2=stack.pop()
            stack.push(op1+' '+op2+' /')
        elif strlst[i] == '**':
            op1=stack.pop()
            op2=stack.pop()
            stack.push(op1+' '+op2+' **')
        elif strlst[i] == '>>':
            op1=stack.pop()
            op2=stack.pop()
            stack.push(op1+' '+op2+' >>')
        elif strlst[i] == '<<':
            op1=stack.pop()
            op2=stack.pop()
            stack.push(op1+' '+op2+' <<')
        else:
        #pushes the operands
            stack.push(strlst[i])
    #the reamining item on the stack should be the new expression
    return stack.pop()