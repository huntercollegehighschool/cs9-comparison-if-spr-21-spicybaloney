'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

a = int(input("enter a number: "))
b = int(input("enter another number: "))
c = int(input("enter a third number: "))

if a < b and a < c :
  smallest = a
  print("the smallest number is", smallest,", yes")
elif b < a and b < c :
  smallest = b
  print("the smallest number is", smallest,", yes")
elif c < a and c < b :
  smallest = c
print("the smallest number is", smallest,", yes")





