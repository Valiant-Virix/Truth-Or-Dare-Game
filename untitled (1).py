# -*- coding: utf-8 -*-
""".ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pXK8XjIAReG4OwVuh1WNnQTHtJ_vXQLe
"""

#Question 1
def AP(a,b):
  op= a*b
  print("a * b =",op)
  def FC():
    print("a * b + 5 =",op+5)
  FC()
AP(2,5)

#Question 2 part a
#2D arrays have 2 lists
#1D has only 1 list

#Question 2 part b
import numpy as np
array1 = np.arange(12,39)
array1

#Question 2 part c
import numpy as np
array1 = np.arange(2,11)
array1

#Task 3 part a
from numpy import random
x = random.rand(5)
print(x)

#Question 3 part b
import numpy as np
b= np.random.randn(3,1,3)
b

#Task 3 part c
import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)

import numpy as np
arr = np.array ([2,3,4,5])
print(np.sort(arr))