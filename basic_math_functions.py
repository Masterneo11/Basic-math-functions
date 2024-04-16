

def add(x: float, y: float) -> float:
    return float(x + y)

def multiply(x: float, y: float) -> float:
    return float(x * y)

def square(x: float) -> float:
    return float(multiply(x,x))

def add_squares(x: float, y: float) -> float:
    return float(add(square(x) ,square(y)))





x = 5
y = 2
print("x = 5")
print("y = 2")

print(f"the add functoin is {add(x,y)} ")
print(f" the multiply function is { multiply(x,y)} ")
print(f" the square function is {square(x,)} ")
print(f" the add squares is {add_squares(x,y)} ")