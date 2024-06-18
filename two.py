#question1
word1 = "Hello"
word2 = "welcome"

index1 = word1.index('o')
index2 = word2.index('o')

combined_word = word1 + word2
result_char = combined_word[index1 + index2]

print("The character at the index position obtained by adding the indices of the character 'o' in the words 'Hello' and 'welcome' is:", result_char)



#question2
single_value_tuple = (5,)
print("The tuple with a single value '5' is:", single_value_tuple)


#question3
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

concat_dict = {}
concat_dict.update(dict1)
concat_dict.update(dict2)

print("The concatenated dictionary is:", concat_dict)


#question4
X = {1, 2, 3, 4}
Y = {5, 6, 7, 8}

if X.isdisjoint(Y):
    print("The sets X and Y are disjoint.")
else:
    print("The sets X and Y are not disjoint.")
    

#question5
my_list = [10, 20, 30, 40, 50]

third_element = my_list[2]

print("The third element in the list is:", third_element)


#question6
num_tuple = (-4, 7, -8, -9, 8, -6, 7, 3, -6, 1, -8, -6)

count = num_tuple.count(-6)

print("The number -6 occurs", count, "times in the tuple.")


#question7
num_list = [5, 3, 6, 1, 85, 23, 5, 13]

if 53 in num_list:
    print("The number 53 is in the list.")
else:
    print("The number 53 is not in the list.")
    
    
#question
numbers = {2, 3, 4, 5}

numbers.discard(3)

print("The updated set is:", numbers)


#question9
num_list = [24, 18, 24, 47, 52]

num_tuple = tuple(num_list)

print("The tuple is:", num_tuple)


#question10
europe = {
    'Spain': {'Capital':'Madrid', 'Population':4.77},
    'France': {'Capital':'Paris', 'Population':6.7},
    'Germany': {'Capital':'Berlin', 'Population':8.28},
    'Norway': {'Capital':'Oslo', 'Population':0.533}
}

germany_capital = europe['Germany']['Capital']

print("The capital of Germany is:", germany_capital)


#question11
num_set = {5, 10, 3, 15, 2, 20, 10, 5, 4, 3}

max_value = max(num_set)

min_value = min(num_set)

print("The maximum value is:", max_value)
print("The minimum value is:", min_value)


