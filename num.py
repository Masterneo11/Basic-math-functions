      


def num_guesser(a, target):
 
 
    left = 0
    right = len(a) -1
 
    while left <= right:
 
        mid = (left + right) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target :
                
        else:
            right = mid - 1
    return -1 

# somehow i have to give the option of going higher or lower to the computer 
# im guessing for conditionals maybe 

a = [ i for i in range(100)]
target = int(input(" enter a number 1-100 : "))
print(num_guesser(a,target))
 



too_high = print(" that was too high ")
too_low = print(" that was too low ")


acquired_guess = is  
