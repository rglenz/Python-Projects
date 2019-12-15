#This fuction finds the max value from a given list 
#list-> int
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list==None or []:
        raise ValueError
        return None
    temp=int_list[0]
    for x in int_list:
        if x>temp:
            temp=x
    return temp    

#This function takes in a list and returns a list that is in reverse order 
#list-> list
def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list==None or []:
        raise ValueError
        return None
    if len(int_list)==1:
        return int_list
    return(reverse_rec(int_list[1:])+int_list[:1])

#this function uses a binary search method to determine if a given target is in a given list or not
#if the value is in the list, the index will be returned
#if not None is returned 
#int int int list -> int
def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list==None or []:
        raise ValueError
        return None
    elif high<low:
        return None
    mid = (high+low)//2
    if target>int_list[high] or target<int_list[low]:
        return None
    if target==int_list[mid]:
        return mid
    elif target==int_list[high]:
        return high
    elif target== int_list[low]:
        return low
    elif target>int_list[mid]:
        low=mid+1
        high=len(int_list)-1
        return(bin_search(target,low, high, int_list))
    elif target<int_list[mid]:
        high=mid-1
        low=0
        return(bin_search(target,low, high, int_list))

    

  


