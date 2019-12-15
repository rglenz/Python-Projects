
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    s=''
    #this handles if the case is greater than 10. 11-16 are represented by A-F
    lst=['A','B','C','D','E','F']
    #find the quotient and remainder of the number by the base 
    quotient=num//b
    remainder=num%b
    #base case 
    if quotient==0:
        if remainder>=10:
            return lst[remainder-10]
        return str(remainder)
    #turn the remainder which is what we return into a string
    s=str(remainder)
    #Recursive step
    if b>10:
        for x in range(6):
            if x+10==remainder:
                return convert(quotient,b)+lst[x]
        return convert(quotient,b)+s
    else:
        return convert(quotient,b)+s
        
    

