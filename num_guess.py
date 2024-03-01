

#Make a number guesser where the program tries to guess your number! You'll pick a number (don't give it to the program), the\#n the program tries to guess it. If it's wrong, you'll tell it whether it was too high or too low, then it'll guess again. Use a binary search algorithm for the guessing.



# do i have to check for my target number 
# wouldnt i have to randomize the 

def num_guesser(a):

    
    left = 0 
    right = len(a) -1 
    
    while target != mid:  # or while left <= right: 
        
        mid = (left + right) // 2

        

        if a[mid] == target:
            return mid
        elif a[mid] < target :
            left = mid + 1
            
        else: 
            right = mid-1

    
        
a = [i for i in range(100)]
print(" Welcome to the number guesser! Pick a number in your mind and I'll try to guess it!")
print()
print(" Are you ready :  ( yes or no : ) " )



decision = input(" yes or no : ")

if decision == "yes":
    print(" Great! ")
    target = int(input("type in a number that is between 1 and 100:  "))
    num_guesser(a)

elif decision == "no":
    print("okay well give you some time just type  ' yes '  when you are ready")




c = target = int(input("type in a number that is between 1 and 100"))
print(num_guesser(a, target))









#Example flow
#Welcome to the number guesser! Pick a number in your mind and I'll try to guess it!

#Are you ready (yes or no): yes

#Great!

#Is it 50 (yes or no): no

#Was that too high or too low (too high or too low): too high

#Is it 25 (yes or no): no

#Was that too high or too low (too high or too low): too high

#Is it 12 (yes or no): no

#Was that too high or too low (too high or too low): too low

#Is it 18 (yes or no): yes

#I got it! Awesome! Thanks for playing!

