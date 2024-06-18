#question1
char = 65

for i in range(1, 7):
    for j in range(i):
        print(chr(char), end=' ')
        char += 1
    print()
    
    
#question2
n = 2
for i in range (1,11):
    print(n, 'x' , i, '=' , n*i)
    
    
#question3
t1=(10, 4, 6, 9)
t2= (5, 2, 3, 3)
print("The original tuple 1 : " + str(t1)) 
print("The original tuple 2 : " + str(t2))

from operator import floordiv
div = tuple(map(floordiv, t1, t2)) 
print('The zipped tuple after dividing is: ' + str(div))


#question4
astro = [['sky', 'sun', 'moon'], ['star', 'Jupiter', 'mars'], ['Jupiter', 'Neptune', 'Pluto']]

short_words = [word for sublist in astro for word in sublist if len(word) < 5]

print(short_words)


#question5
original_tuple = (4, 5, 6)
dictionary_to_add = {'gfg': 1, 'is': 2, 'best': 3}

new_tuple = original_tuple + (dictionary_to_add,)

print(new_tuple)


#question6
def check_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if check_anagram(str1, str2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
    
    
#question7
fruity = {'Fruits 01' : 'Apple', 'Fruits 02' : 'Orange', 'Fruits 0 3 ': 'Grapes'}

new_fruity = {}

for key, value in fruity.items():
    new_key = key.replace(" ", "")
    new_fruity[new_key] = value

print("New dictionary:", new_fruity)


#question8
matrix = [[1,2],[3,4],[5,6],[7,8]]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Original matrix:", matrix)
print("Transposed matrix:", transposed_matrix)


#question9
i = 1
sum_of_cubes = 0

while i <= 5:
    sum_of_cubes += i ** 3
    i += 1

print("The sum of the cubes of the first 5 positive integers is:", sum_of_cubes)


#question10
matrix = [[1, 2, 3] for _ in range(5)]

print("Matrix:")
for row in matrix:
    print(row)

