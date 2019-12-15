def bears(n):
    '''A True return value means that it is possible to win
 the bear game by starting with n bears. A False return value means
 that it is not possible to win the bear game by starting with n
 bears.'''
    #base case for winning the game 
    if n==42:
        return True
    #base case for losing the game 
    if 42>n:
        return False
    #Recursive step
    #handles if you have a number of bears divisible by 5
    if n%5==0 and bears(n-42):
        return True
    n=int(n)
    #this retrives the last digit in an int 
    n1=int(str(n)[-1])
    #this will get the second to last digit in an int
    n2=int(str(n)[-2])
    #handles if amount of bears is divisible by 3 or 4
    if n%3==0 or n%4==0 and n1!=0 and n2!=0 and bears(n-n1*n2):
        return True
    #handles if the amount of bears is even 
    if n%2==0 and bears(n-int(n/2)):
        return True
    
    return False

    
    
    

