from matplotlib import pyplot as plt
import numpy as np

A = np.array([1, 2, 3, 4, 5])
B = np.array([3.1, 5, 4, 6])
D = np.array([1, 2, 'a', 3])
D.dtype
D.dtype.type
D.dtype.itemsize

C = np.array([1, 2, 3, 8], dtype=float)
print(C)

# create vector of length 5 filled with zeros
E = np.zeros(5, dtype=float)

# create 2x4 matrix of ones (float)
F = np.ones((2, 4), dtype=float)

# create vector from 0-12 in steps of 2
G = np.arange(0, 12, 2)

# create vector from 0 to 1 with five equally (linearly) spaced elements
H = np.linspace(0, 1, 5)

# create a 2x2 matrix with random floats in the half-open interval [0.0, 1.0)
I = np.random.random((2, 2))

# Return random integers from 0 (inclusive) to 10 (exclusive) of size (4,3,2)
J = np.random.randint(0, 10, (4, 3, 2))

print("E =", E,  "\n\nF =", F,  "\n\nG =", G,
      "\n\nH =", H,  "\n\nI =", I,  "\n\nJ =", J)

print("E =", E, "\n\nF =", F)


# ______________

# Your code here
i = 10
for i in range(1, 11):
    arr = np.random.randint(low=1, high=(i+1), size=i)
    print(arr)


# returns dimension
print("E ndim: ", E.ndim)

# returns shape in form (#row,#col)
print("F sahpe: ", F.shape)

# returns size (i.e. no of elements)
print("J size: ", J.size)

# returns data type
print("H dtype: ", H.dtype)

# returns length of one array element in bytes
print("itemsize: ", I.itemsize, " bytes")

# returns total bytes consumed by the elements of the array
print("nbytes:  ", I.nbytes, "bytes")


print(A)
A[-2]

print("The 4th element of A is {}". format(A[3]))
print("The last element of A is {}". format(A[-1]))  # index from the back


I[1, 1]


print("The first element of I is {}". format(I[0, 0]))  # array[row,column]
print("The last element of I is {}". format(I[1, 1]))  # array[row,column]

G

# item 3 and 4
print("middle subarray:", G[2:4])

# item 1 to 4(excl.)
print("First 4 elemnts:", G[:5])

# last 3
print("Last 3 elements:", G[-3:])

# first element and every second from there
print("Every other element:", G[::2])


print("All elements reversed:", G[::-1])

K = np.random.randint(0, 20, (3, 4))

K

print("The first two rows and the first three column: \n", K[:2, :3])

print("All rows and every other column:\n", K[:, ::2])

print("Reversed:\n", K[::-1, ::-1])

# return evenly spaced values within a given interval
Y = np.arange(1, 25)
Y


len(Y)

# we can re-shape this array into any shape with 24 elements

Y.reshape(6, 4)

# Your code heres
print("transpose:")
print(K[:2, :2].T)

# important to understand that "reshape" cannot help here!´

KK = np.array([K, K])
KK

KK.transpose(0, 2, 1)  # T is just shorthand for transpose

P = np.array([1, 2, 3])
Q = np.array([4, 5, 6])
np.concatenate((P, Q))

R = np.array([[3, 5, 7], [1, 3, 5]])
S = np.array([[2, 4, 2], [0, 9, 8]])

# The axis along which the arrays will be joined.
print(np.concatenate((R, S), axis=0))


arr1 = np.load('array1.np')
arr2 = np.load('array2.npy')

array = np.hstack([arr1.transpose(1, 0, 2), arr2.transpose(1, 0, 2)])

plt.imshow(array)

plt.imshow(arr2)
plt.imshow
# .......


plt
