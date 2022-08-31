# Part 1
# Calculate simple interest by gathering three things (principle, number of years, rate of interest).

p = int(input("Please enter Principle: "))
n = int(input("Please enter Number of Years: "))
r = int(input("Please enter Rate of Interest: "))

# Calculate the simple interest of p, n, r (multiple p, n, r, and then divide by 100).

ans = (p * n * r)/100

# Print out the simple interest value

print(ans)

# Part 2
# Create a list of your favorite food items, the list should have a minimum of 5 elements.

favFoods = ["ice cream", "chocolate", "roast", "mashed potatoes", "pizza"]

# List out the 3rd element in the list.

print(favFoods[2])

# Add additional items to the current list and display the list.

# Insert an element named tacos at the 3rd index position of the list and print out the list elements.

favFoods.insert(2, "Tacos")

print(favFoods)

# Part 3
# Using a for-loop and a range function, print "I am a programmer" 5 times.

for x in range(1, 6):
    print("I am a programmer")

# Create a function that displays out the square values of numbers from 1 to 9.

def square():
    for y in range(1, 9):
        print(y * y)

square()