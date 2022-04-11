#!/usr/bin/env python

#Import libraries
#
import numpy as np
import sys

#Getting matrices from files on the command line
#
matrix1=np.loadtxt(sys.argv[1],dtype=float,delimiter=' ')
matrix2=np.loadtxt(sys.argv[2],dtype=float,delimiter=' ')

#Matrices and dimensions
#
row1=len(matrix1)
col1=len(matrix1[0])
row2=len(matrix2)
col2=len(matrix2[0])

#Making sure matrix dimension are within the range of 1 to 100
#
if(row1<=1 or row2<=1 or col1<=1 or col2<=1 or row1>=100 or row2>=100 or col1>=100 or col2>=100):
    #Error message if dimensions are uneven
    #
    print('Rows and columns of matrices invalid')
    sys.exit(0)

#Multiplication error check
#
elif col1!=row2 or row1!=col2:
    print('Error colums and rows are uneven')
    sys.exit(0)

#Multiplication operation being done
#
else:

    #Result is being calculated
 result = np.zeros(row1*col2).reshape((row1,col2))

    #Looping through rows of matrix1
    #
    for i in range(len(matrix1)):

        #Looping through columns of matrix2
        #
        for j in range(len(matrix2[0])):

            #Looping through rows of matrix2
            #
            for k in range(len(matrix2)):

                #Storing results
                #
                result[i][j] += matrix1[i][k] * matrix2[k][j]

                #Formatting output matrix
                #
                result = np.matmul(matrix1,matrix2)

#Printing the result
#
print(result)
