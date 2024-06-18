#question1
lsbool = ['True','FALse','tRUe','tRue','False','faLse','True']

result = list(map(lambda x: x.upper(), lsbool))

print("Original List:", lsbool)
print("List in Uppercase:", result)

#question2
def print_student_heights(student_heights):
    total_height = 0
    for height in student_heights:
        print(f"The height of student {student_heights.index(height)+1} is {height} inches.")
        total_height += height
    print(f"The total height of the class is {total_height} inches.")


#question3
import math

func_dict = {
    'Square': lambda x: x ** 2,
    'Cube': lambda x: x ** 3,
    'Squareroot': lambda x: math.sqrt(x),
    'Double': lambda x: x * 2
}

num = float(input("Enter a number: "))

result_sum = 0

for func_name, func in func_dict.items():
    result = func(num)
    print(f"The {func_name} of {num} is {result}")
    result_sum += result

print(f"The sum of the results is {result_sum}")


#question4
def find_words_with_uppercase_second_char(word_list):
    return [word for word in word_list if len(word) > 1 and word[1].isupper()]

ls = ['hello', 'Dear', 'hOw', 'ARe', 'You']
print(find_words_with_uppercase_second_char(ls))


#question5
def filter_marks_and_print_names(tnames, tmarks):
    for name, mark in zip(tnames, tmarks):
        if mark > 40:
            print(f"Name: {name}, Mark: {mark}")

tnames = ('John','Sharon','Jack','Annie')
tmarks = (32,50,75,12)
filter_marks_and_print_names(tnames, tmarks)


#question6
WeightOnEarth = {'John':45, 'Shelly':65, 'Marry':35}
GMoon = 1.622
GEarth = 9.81

weight_on_moon = dict(map(lambda item: (item[0], round(item[1] * GMoon / GEarth, 2)), WeightOnEarth.items()))
print("Weight on Moon:", weight_on_moon)


#question7
from functools 

given_sets = [[1, 2, 3, 4, 8], [2, 3, 8, 5, 6], [8, 4, 5, 3, 7], [6, 9, 8, 3], [9, 12, 3, 7, 6, 8, 4, 6, 21, 1, 6]]

print (functools.reduce(lambda x,y:set(x)&set(y),given_sets))

#question8
def store_product_prices():
    product_prices = {}
    while True:
        product = input("Enter product name (or 'quit' to finish): ")
        if product.lower() == 'quit':
            break
        product_prices[product] = float(input("Enter price of {}: ".format(product)))
    return product_prices

product_prices = store_product_prices()
print("\n".join(f"{product}: ${price:.2f}" for product, price in product_prices.items()))


#question9
def multiply(a, b):
    return a * b

a = 16
b = 12
print(multiply(a, b)) 


#question10
from itertools import accumulate
from functools import reduce
from operator import add

input_list = [9, 8, 7, 6, 5]

cumulative_averages = list(accumulate(input_list, lambda x, y: (x + y) / 2))

print(cumulative_averages)

