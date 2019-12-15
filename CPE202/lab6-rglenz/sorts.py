import random
import time
def selection_sort(list):
    cnt=0
    for fillslot in range(len(list)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            cnt+=1
            if list[location]>list[positionOfMax]:
                positionOfMax = location

        temp = list[fillslot]
        list[fillslot] = list[positionOfMax]
        list[positionOfMax] = temp
    return cnt

def insertion_sort(list):
    # for every element in our array
    cnt=0
    for index in range(1,len(list)):
        currentvalue = list[index]
        position = index
        while position>0:
            cnt+=1
            if list[position-1]>currentvalue:
                
                list[position]=list[position-1]
                position = position-1
            else:
                break
        list[position]=currentvalue
    return cnt


def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 16000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

