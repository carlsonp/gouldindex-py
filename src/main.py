from scipy import linalg
import scipy.sparse.linalg as sparse
import numpy as np
import sys

#Ignore conversion from imaginary to real number
np.warnings.simplefilter("ignore", np.ComplexWarning)

# Data from previous Java example
# data = np.array([ [1, 1, 1, 0, 0, 0, 0],
#                 [1, 1, 1, 0, 0, 0, 0],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [0, 0, 1, 1, 1, 0, 0],
#                 [0, 0, 1, 1, 1, 0, 0],
#                 [0, 0, 1, 0, 0, 1, 1],
#                 [0, 0, 1, 0, 0, 1, 1] ] )

#New example data
# data = np.array([ [1, 0, 1, 0, 1, 1, 0, 0, 0],
#                 [0, 1, 1, 0, 0, 0, 1, 0, 0],
#                 [1, 1, 1, 1, 0, 0, 0, 1, 0],
#                 [0, 0, 1, 1, 1, 0, 0, 0, 1],
#                 [1, 0, 0, 1, 1, 0, 0, 1, 0],
#                 [1, 0, 0, 0, 0, 1, 1, 0, 0],
#                 [0, 1, 0, 0, 0, 1, 1, 0, 0],
#                 [0, 0, 1, 0, 1, 0, 0, 1, 1],
#                 [0, 0, 0, 1, 0, 0, 0, 1, 1] ] )

# Generate random data (to test how long this will take on larger datasets)
data = np.random.randint(2, size=(1000, 1000))
data = (data + data.T)/2 #make it symmetrical
print "Finished generating data."

#use this for non-sparse matrices
#eigenvalues,eigenvectors = linalg.eig(data)
#on sparse matrices, this should be faster
eigenvalues,eigenvectors = sparse.eigs(data.astype(float))
print "Eigenvalues:"
print eigenvalues.round().astype(int)

print "Eigenvalues after absolute value:"
abs_eigenvalues = np.absolute(eigenvalues.round().astype(int))
print abs_eigenvalues

print "Principle Eigenvalue (largest):"
principle_eigenvalue = np.amax(abs_eigenvalues)
print principle_eigenvalue

print "Principle Eigenvalue Index:"
principle_index = np.where(abs_eigenvalues == principle_eigenvalue)[0][0]
print principle_index

print "Eigenvectors:"
eigenvectors = eigenvectors.astype(float)
print eigenvectors

print "Eigenvectors associated with principle eigenvalue index:"
eigenvectors_index = eigenvectors[:,[principle_index]]
print eigenvectors_index

print "Sum of Eigenvectors Associated with Principle Eigenvalue Index:"
sum_eig = eigenvectors_index.sum()
print sum_eig

print "Normalized Eigenvectors (Gould Index values for each node):"
normalized_eigenvectors = []
for x in np.nditer(eigenvectors_index):
    normalized_eigenvectors.append(round(x * (1/sum_eig), 3))
print normalized_eigenvectors

print "Largest Gould Index:"
print np.amax(normalized_eigenvectors)

print "Smallest Gould Index:"
print np.amin(normalized_eigenvectors)

