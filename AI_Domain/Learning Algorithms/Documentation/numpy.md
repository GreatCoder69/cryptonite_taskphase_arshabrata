# Numpy for Machine Learning
## Introduction
NumPy (Numerical Python) is a fundamental library in Python for numerical and scientific computing. It provides powerful tools for working with arrays, matrices, and large multidimensional datasets, which makes it essential for data science, machine learning, and engineering applications. With its high-speed array processing and wide array of mathematical functions, NumPy is a vital tool for handling and manipulating data efficiently.
## Downloading and importing pandas
```
pip install numpy
```
We must first install the numpy libraries.
```
import numpy as np
```
This imports the necessary packages for numpy.
### Using Numpy
```
list=[0,1,2,3,4,5]
np1=np.array(list)
```
Converts the list to a numpy array.
```
np1.shape
```
This gives us the shape/dimensions of the array
```
np2=np.arange(10)
```
This fills values from 0 to 9 (10 values)
```
np3=np.arange(0,10,2)
```
Gets numbers from 0 to 9 incrementing by steps of 2.
```
np4=np.zeros(10)
```
Creates a vector of 1X10 dimension containing only zeros.
```
np5=np.zeros(2,10)
```
Creates a vector of 2X10 dimension containing only zeros.
```
np6=np.full((2,10),6)
```
Creates an array of 2X10 dimension filled with only 6.
```
np1[3]
```
Gets the element at index 3.
```
np1[1:5]
```
This pulls all elements from index 1 to index 4 (excluding index 5).
```
np1[3:]
```
This pulls all elements from index 3 till the end. Slicing can also be negative.
```
np1[1:5:2]
```
Gets elements from index 1 to index 4 with steps of 2.
```
np1[1:4,2:5]
```
Slicing in range.
```
np.sqrt(np1)
```
Finds square root of every element.
```
np.absolute(np1)
```
Takes distance from zero, so basically makes all values positive.
```
np.exp(np1)
```
We get the exponentials for every item.
```
np.min(np1)
np.max(np1)
```
Gives us the minimum and maximum values in the numpy.
```
np.sign(np1)
```
When no. is positive, the array element takes the value +1.  
When no. is 0, the array element takes the value 0.  
When no. is negative, the array element takes the value -1.
```
np.sin(np1)
np.cos(np1)
np.tan(np1)
np.log(np1)
```
We can perform mathematical functions on numpy.
```
np2=np1.view()
```
When we change a value in the original, the change is also reflected in the copied numpy. There exists a link with the original numpy.
```
np2=np1.copy()
```
When we change a value in the original, the change is not reflected in the copied numpy. There exists no link with the original.
```
np1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
np2=np1.reshape(3,4)
np3=np1.reshape(2,3,2)
```
Reshapes the array into 3 rows and 4 columns for np2.  
Reshapes the array into 3 dimensions of 2,3 and 2 values for np3.
```
np4=np3.reshape(-1)
```
Flattens the array back to a 1D array.
```
for x in np1:
    for y in x:
        print(y)
```
Prints all the elements in the numpy.
```
for x in np.nditer(np3):
    print(x)
```
This prints all the elements in the array for any n-dimensional numpy.
```
np.sort(np1)
```
Sorts in ascending order. Works even for strings and boolean.  
For boolean, false comes before true as false is 0 and true is 1.
Note: Using sort does not change the original array. We only change the output for that line.
```
x=np.where(np1==3)
```
Returns a tuple of index numbers where 3 is present in np1.
```
y=np.where(np1%2==0)
```
Returns all even numbers. We can use any conditional operator with the where function.
```
np1=np.array[1,2,3,4,5]
x=[True,False,False,True,False]
print(np1[x])
```
This will print only the numbers corresponding to True.
```
filtered=[]
for thing in np1:
    if thing%2==0:
        filtered.append(True)
    else:
        filtered.append(False)
print(np1[filtered])
```
This will only print the even numbers in the numpy.
```
filtered=(np1%2==0)
print(np1[filtered])
```
Shortcut to print the even numbers in the numpy.
