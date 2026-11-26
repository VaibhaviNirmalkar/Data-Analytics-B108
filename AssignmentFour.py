# import numpy as np

# Q1 How do you create a NumPy array from the list [1, 2, 3, 4, 5]?


# arr = np.array([1, 2, 3, 4, 5])
# print(arr)



# Q2 What is the output of np.array([10, 20, 30, 40])[2]?

# arr = np.array([10, 20, 30, 40])
# print(arr[2])



# Q3 Create a NumPy array containing integers from 1 to 10.

# arr = np.arange(1, 11)
# print(arr)



# Q4 Create a NumPy array containing five zeros.

# arr = np.zeros(5)
# print(arr)



# Q5 Create a 3 × 3 NumPy array containing only ones.

# arr = np.ones((3, 3))
# print(arr)



# Q6 What is the shape of np.array([[1, 2, 3], [4, 5, 6]])?

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)



# Q7 What is the number of dimensions of np.array([[1, 2], [3, 4], [5, 6]])?

# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr.ndim)



# Q8 Given arr = np.array([10, 20, 30, 40, 50]), extract the elements from index 1 to index 3.

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[1:4])



# Q9 Given arr = np.array([1, 2, 3, 4, 5]), multiply every element by 10.

# arr = np.array([1, 2, 3, 4, 5])
# print(arr * 10)



# Q10 Find the sum, mean, maximum, and minimum of np.array([12, 5, 8, 20, 15]).

# arr = np.array([12, 5, 8, 20, 15])

# print("Sum:", np.sum(arr))
# print("Mean:", np.mean(arr))
# print("Maximum:", np.max(arr))
# print("Minimum:", np.min(arr))



# Q11 Given arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), extract only the even numbers.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(arr[arr % 2 == 0])



# Q12 Sort np.array([5, 2, 8, 1, 9, 3]) in ascending order.

# arr = np.array([5, 2, 8, 1, 9, 3])
# print(np.sort(arr))



# Q13 Find the indices of elements greater than 50 in np.array([10, 60, 30, 80, 45, 90]).

# arr = np.array([10, 60, 30, 80, 45, 90])

# print(np.where(arr > 50))



# Q14 Reshape np.array([1, 2, 3, 4, 5, 6]) into a 2 × 3 array.

# arr = np.array([1, 2, 3, 4, 5, 6])

# print(arr.reshape(2, 3))



# Q15 Given two arrays [1, 2, 3] and [4, 5, 6], perform element-wise addition, subtraction, multiplication, and division.

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)



# Q16 Perform matrix multiplication on [[1, 2], [3, 4]] and [[5, 6], [7, 8]].

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# print(np.dot(a, b))



# Q17 Find the transpose of [[1, 2, 3], [4, 5, 6]].

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# print(arr.T)



# Q18 Replace all values greater than 3 with 100 in np.array([1, 2, 3, 4, 5]).

# arr = np.array([1, 2, 3, 4, 5])

# arr[arr > 3] = 100
# print(arr)



# Q19 Create a 5 × 5 array containing numbers from 1 to 25 and extract the second row and third column.

# arr = np.arange(1, 26).reshape(5, 5)

# print("Second row:", arr[1])
# print("Third column:", arr[:, 2])



# Q20 Given [[10, 20, 30], [40, 50, 60], [70, 80, 90]], find the row sums, column sums, overall mean, and elements greater than 45.

# arr = np.array([[10, 20, 30],
#                 [40, 50, 60],
#                 [70, 80, 90]])

# print("Row sums:", np.sum(arr, axis=1))
# print("Column sums:", np.sum(arr, axis=0))
# print("Mean:", np.mean(arr))
# print("Greater than 45:", arr[arr > 45])



# Q21 Create a NumPy array containing all even numbers from 2 to 20.

# arr = np.arange(2, 21, 2)
# print(arr)



# Q22 Create a NumPy array containing 10 equally spaced values between 0 and 1.

# arr = np.linspace(0, 1, 10)
# print(arr)



# Q23 Given arr = np.array([3, 7, 2, 9, 4, 8]), find the index of the maximum value.

# arr = np.array([3, 7, 2, 9, 4, 8])

# print(np.argmax(arr))



# Q24 Given arr = np.array([10, 20, 30, 40, 50]), reverse the array.

# arr = np.array([10, 20, 30, 40, 50])

# print(arr[::-1])



# Q25 Find the unique values in np.array([1, 2, 2, 3, 4, 4, 5]).

# arr = np.array([1, 2, 2, 3, 4, 4, 5])

# print(np.unique(arr))



# Q26 Count how many elements are greater than 25 in np.array([10, 30, 15, 40, 25, 50]).

# arr = np.array([10, 30, 15, 40, 25, 50])

# print(np.sum(arr > 25))



# Q27 Convert the following 1D array into a 3 × 3 array: np.array([1,2,3,4,5,6,7,8,9]).

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(arr.reshape(3, 3))



# Q28 Flatten the array [[1, 2], [3, 4], [5, 6]] into a 1D array.

# arr = np.array([[1, 2], [3, 4], [5, 6]])

# print(arr.flatten())



# Q29 Concatenate np.array([1,2,3]) and np.array([4,5,6]).

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.concatenate((a, b)))



# Q30 Split np.array([1,2,3,4,5,6]) into three equal parts.

# arr = np.array([1, 2, 3, 4, 5, 6])

# print(np.split(arr, 3))



# Q31 Find the standard deviation of np.array([10, 20, 30, 40, 50]).

# arr = np.array([10, 20, 30, 40, 50])

# print(np.std(arr))



# Q32 Find the variance of np.array([2, 4, 6, 8, 10]).

# arr = np.array([2, 4, 6, 8, 10])

# print(np.var(arr))



# Q33 Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative sum.

# arr = np.array([1, 2, 3, 4, 5])

# print(np.cumsum(arr))



# Q34 Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative product.

# arr = np.array([1, 2, 3, 4, 5])

# print(np.cumprod(arr))



# Q35 Replace all odd numbers with -1 in np.array([1,2,3,4,5,6,7]).

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# arr[arr % 2 != 0] = -1
# print(arr)



# Q36 Find the maximum value in each row of [[1,5,3],[8,2,6],[4,9,7]].

# arr = np.array([[1, 5, 3],
#                 [8, 2, 6],
#                 [4, 9, 7]])

# print(np.max(arr, axis=1))



# Q37 Find the minimum value in each column of [[5,2,8],[1,7,3],[6,4,9]].

# arr = np.array([[5, 2, 8],
#                 [1, 7, 3],
#                 [6, 4, 9]])

# print(np.min(arr, axis=0))



# Q38 Create a 4 × 4 identity matrix using NumPy.

# arr = np.eye(4)
# print(arr)



# Q39 Generate a 3 × 3 matrix of random integers between 1 and 20.

# arr = np.random.randint(1, 21, (3, 3))
# print(arr)



# Q40 Given two NumPy arrays, find the elements that are common to both arrays.

# a = np.array([1, 2, 3, 4, 5])
# b = np.array([3, 4, 5, 6, 7])

# print(np.intersect1d(a, b))