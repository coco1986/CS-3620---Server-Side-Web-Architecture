# Part 1
# 1. Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
#       - BMI = (weight in Kg)/(Height in Meters)^2.
# 2. Write code that can accept the weight and height of a person and calculate their BMI.
#       - Make sure to use a function that accepts the height and weight values and returns the BMI value.
def bmi_calculator(calc_weight, calc_height):
    calc_bmi = calc_weight / (calc_height ** 2)
    return calc_bmi


weight = float(input("Enter your weight in Kilograms: "))
height = float(input("Enter your height in Meters: "))
bmi = bmi_calculator(weight, height)
print(bmi)

# Part 2
# 1. Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero
# exception.
try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('There is a divide by zero error!')
finally:
    print('I find your lack of a denominator disturbing')

# Part 3
# 1. Write Python code to open a file named demo.txt and write some random data into it.
# 2. Open the file, read the contents, and display them as output.
# 3. Write code to add additional text to the existing file on a new line without deleting the previous contents.
file = open('demo.txt', 'w')
file.write('this is text')
file.close()

file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('demo.txt', 'a')
file.write('This is more text')
file.close()

# Part 4
# 1. Write code that accepts the name of a product and in turn returns their respective prices.
#       - Make sure to use a dictionary to store products and their respective prices.
#       - The dictionary should include at least 5 elements.
products = {
    "guitar": "$1200",
    "strings": "$20",
    "distortion pedal": "$75",
    "picks": "$5",
    "amplifier": "$250",
}
enter_product = input("Enter in a product: ")
if enter_product in products:
    print(products.get(enter_product))
else:
    print("Product Not Found")

# Part 5
# 1. List out all the odd numbers from 1 to 100 using lists in Python.
#       - use list(), range(), and a for loop with a conditional statement that outputs the numbers.
num_list = list(range(1, 100))
for x in num_list:
    if x % 2 != 0:
        print(x)