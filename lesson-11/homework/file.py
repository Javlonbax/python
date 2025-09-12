# Create your own virtual environment and install some python packages.
python -m venv myenv
myenv\Scripts\activate
pip install requests numpy pandas

# Create custom modules
#Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
#Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
def reverse(s):
    return "".join(reversed(s))
print(reverse("asdfgh"))
def count_vowels(s):
    vowels="aiuoe"
    count=0
    for i in s:
        if i.lower() in vowels:
            count+=1
    return count
print(count_vowels("asdfghjuioklrtewq"))

# Create custom packages.
#Create geometry package.
def area_circle(radius):
    return 3.14159 * radius * radius

def area_rectangle(length, width):
    return length * width

def perimeter_square(side):
    return 4 * side

# Create file_operations package.
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
