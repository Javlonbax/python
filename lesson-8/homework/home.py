# Exception Handling Exercises
# 1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def calc(n):
  try:
    return 1/n
  except ZeroDivisionError:
    return 'Noldan boshqa son kirit!'
print(calc(2))

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer
def calc(n):
  try:
    return 1/int(n)
  except ValueError:
    return 'Raqam kirit!'

print(calc(input('Son kiriting '))) 

# 3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
