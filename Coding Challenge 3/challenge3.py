# Part 1
# 1. Assume you want to build two functions for discounting products on a website.
#     - Function number 1 is for student discount which discounts the current price by 10%.
#     - Function number 2 is for an additional discount for regular buyers which discounts an additional 5%
#       on the current student discounted price.
#     - Depending on the situation, we want to be able to apply both discounts on the products.
# 2. Design the above two mentioned functions and apply them both simultaneously on the price.


def student_discount(x):
    y = x
    x = x * .1
    x = y - x
    return x


def regular_discount(x):
    y = x
    x = x * .05
    x = y - x
    return x


print(regular_discount(student_discount(2.99)))


# Part 2     Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.


print((lambda x: x * (x + 5)**2)(5))


# Part 3

# Consider a list in Python which includes prices of all the items in a store.
# Build a function to discount the price of all the products by 10 %.
# Use a map to apply the function to all the elements of the list so that all the product prices are discounted.


def store_discount(x):
    y = x
    x = x * .1
    x = y - x
    return x


storePrices = [5.99, 3.49, 10.50, 6.99, 21.32]

result = list(map(store_discount, storePrices))
print(result)


# Part 4
#
# Using the concept of object-oriented programming and inheritance, create a superclass named Computer, which has
# two subclasses named Desktop and Laptop.
# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications
# and display the specifications of the computer.
#
#
# You can use any specifications that you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them
# for example laptop can have weight as a special specification.
#
#
# Make sure that the subclasses have their own methods to get and display their special specification.
# Create an object of laptop / desktop and make sure to call all the methods from the computer
# class as well as the methods from the own class.


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def get_specs(self):
        self.cpu = input("Input CPU type: ")
        self.ram = input("Input amount of ram in Gigs: ")

    def display_specs(self):
        print("CPU: " + self.cpu + " Ram: " + self.ram)


class Desktop(Computer):
    def __init__(self, gpu):
        super().__init__(self, gpu)
        self.gpu = gpu

    def get_desk_spec(self):
        self.gpu = input("Input GPU type: ")

    def display_desk_spec(self):
        print("GPU: " + self.gpu)


class Laptop(Computer):
    def __init__(self, weight):
        super().__init__(self, weight)
        self.weight = weight

    def get_laptop_spec(self):
        self.weight = input("Input weight: ")

    def display_laptop_spec(self):
        print("Weight :" + self.weight)


asus = Laptop("")
alien = Desktop("")

asus.get_specs()
asus.get_laptop_spec()
asus.display_specs()
asus.display_laptop_spec()

alien.get_specs()
alien.get_desk_spec()
alien.display_specs()
alien.display_desk_spec()


# Part 5

# 1. Using the concept of operator overloading in Python, change the behavior of the multiplication
#    operator in a way that multiplication operator behaves like an addition operator.


class Multi:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return Multi(x)

    def __str__(self):
        return "({0})".format(self.x)


multi1 = Multi(3)
multi2 = Multi(4)
print(multi1 * multi2)
