#Q1a
import numpy as np
vector_arange=np.arange(0,101,10)
print(vector_arange)
#Q1b
vector_linspace=np.linspace(0,100,11)
print(vector_linspace)
#Q1c
vector_short=vector_linspace[:-1]#removing last number from the vector by slicing
matrix = vector_short.reshape(5, 2)#presenting the vector as a 5*2 matrix
print(matrix)