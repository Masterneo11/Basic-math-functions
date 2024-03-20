      


def num_guesser(a):
 
 
    left = 0
    right = len(a) 
    
    while left <= right:
 
        mid = (left + right) // 2
        correct = input(f" is {mid} correct  yes or no: ")
        print()
        
        if correct == "yes":
            print()
            return mid 
        
        higher_lower = input( " do i go higher or lower : ")
       
        
        if higher_lower  == "higher":
            left = mid - 1 
            print()
        
        elif higher_lower == "lower":
            right = mid + 1
            print()

 




a = [ i for i in range(100)]

print()
print()
print(" Welcome to the number guesser! Pick a number in your mind and I'll try to guess it!")
print()
print(" Are you ready :  ( yes or no : ) " )

print()

decision = input(" yes or no : ")

if decision == "yes":
    print(" Great! ")
    print()
    num_guesser(a)

elif decision == "no":
    no = print("okay well give you some time just type  ' yes '  when you are ready")
    yess = input()
    if yess == "yes":
        print()
        print(" Great ! ")
        print()
        num_guesser(a)

 
