#1. Convert List to 1D Array
import numpy as np
list=['a','b','c']
arr=np.array(list)

## 2. Create 3x3 Matrix (2?10)
import numpy as np

matrisa = np.arange(2, 11).reshape(3, 3)

## Null Vector (10) & Update Sixth Value
import numpy as np

v = np.zeros(10)
print("Nolli vektor:", v)
v[5] = 99   
print("O`zgardi:", v)

## Array from 12 to 38
import numpy as np

arr = np.arange(12,38)
print(arr)

## 5. Convert Array to Float Type
import numpy as np

lst=[1,2,3,4]
arr = np.array([1,2,3,4])
arr=arr.astype(float)
print(arr)

## 6. Celsius to Fahrenheit Conversion
import numpy as np

celsius = np.array([0, 20, 37, 100])
fahrenheit = celsius * 9/5 + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

##7. Append Values to Array (Do self-tudy)
import numpy as np

arr=np.array([10, 20, 30])
arr=np.append(arr,[40,50,60])
print(arr)

## 8. Array Statistical Functions (Do self-tudy)
import numpy as np

arr=np.random.randint(0,100,10)
med=np.mean(arr)
mean=np.mean(arr)
std=np.std(arr)
print(arr,med,mean,std)

## 9 Find min and max
import numpy as np

arr=np.random.randint(0,100,10)
min=np.min(arr)
max=np.max(arr)

print(min,max)

## Create a 3x3x3 array with random values.
import numpy as np

arr=np.random.randint(0,100,27).reshape(3,3,3)
print(arr)
