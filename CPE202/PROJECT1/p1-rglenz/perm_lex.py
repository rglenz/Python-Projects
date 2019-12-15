#assume a contains a string of 0 or more lowercase alphabetical ordered letters
def perm_gen_lex(a):
    '''This function will take in string of lowercase letters in
    in alphabetical order and recursively create a list filled with 
    strings of all permutations of the initial string. The list will
    be returned in dictionary order.''' 
    #takes care of empty string
    if a=='':
        return []
    #takes care of single length strings
    #base case
    if len(a)==1:
        return [a]
    flst=[]
    #recursive step goes through every letter and runs
    for i in range(len(a)):
        other=a[:i]+a[i+1:]
        perms=perm_gen_lex(other)
        for x in perms:
            flst.append(a[i]+x)
    return(flst)
    