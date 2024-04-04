def num_guesser(a):
    left = 0
    right = len(a) - 1
    
    while left < right:
        mid = (left + right) // 2
        correct = input(f"Is {mid} correct? (yes or no): ")
        print()
        
        if correct == "yes":
            return f"Great! This must be your number: {mid}"
        
        higher_lower = input("Should I go higher or lower? ")
        
        if higher_lower == "higher":
            left = mid + 1 
            print()
        elif higher_lower == "lower":
            right = mid - 1
            print()
        else:
            print("Invalid input!")


a = [i for i in range(101)]  # Changed to 101 to include 100

print()
print()
print("Welcome to the number guesser! Pick a number in your mind and I'll try to guess it!")
print()
print("Are you ready? (yes or no): ")
print()
decision = input()

if decision == "yes":
    print("Great!")
    print()
    print(num_guesser(a))
elif decision == "no":
    print("Okay, we'll give you some time. Just type 'yes' when you are ready.")
    yess = input()
    if yess == "yes":
        print("Great!")
        print()
        print(num_guesser(a))
