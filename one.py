#question1
pi = 22/7
pi_int = int(pi)
print(pi_int)


#question2
remainder = 542 % 16
print(remainder)


#question3
print("""
                                 *
                                **
                               ***
                              ****
""")



#question4
letter = get_letter_input()

vowels = ['a', 'e', 'i', 'o', 'u']

if letter in vowels:
  print("The letter is a vowel.")
else:
  print("The letter is not a vowel.")
  
  
 #question5

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

num1, num2 = num2, num1

print("Swapped integers: ", num1, num2)


#question6
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))


print("The product of", x, "and", y, "is:", x * y)
  
  
  
#question7
INPUT num
IF num MOD 2 == 0 THEN
  PRINT "Number is even"
ELSE
  PRINT "Number is odd"
ENDIF
  
  
  #question8
  INPUT a
IF a % 2 == 0 AND a % 9 == 0 THEN
  PRINT "Condition satisfied"
ELSE
  PRINT "Condition not satisfied"
ENDIF

#question9
SET sum = 0
SET i = 1

WHILE i <= 5 DO
  INPUT value
  sum = sum + value
  i = i + 1
ENDWHILE

SET average = sum / 5
PRINT "The average is: " + average
  
  
  