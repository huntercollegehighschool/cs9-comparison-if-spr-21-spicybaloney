'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below

month = str(input("enter a month: "))

if month == "september" or month == "april" or month == "june" or month == "november":
  print("there are 30 days in this month")
elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "december":
  print("there are 31 days in this month")
elif month == "february":
  print("there are 28-29 days in this month")
else:
  print("this is not a month")