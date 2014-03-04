from scipy import linalg
from numpy import array, warnings, ComplexWarning, absolute, amax, amin, where, nditer, random


#Ignore conversion from imaginary to real number
warnings.simplefilter("ignore", ComplexWarning)

# Data from previous Java example
# data = array([ [1, 1, 1, 0, 0, 0, 0],
#                 [1, 1, 1, 0, 0, 0, 0],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [0, 0, 1, 1, 1, 0, 0],
#                 [0, 0, 1, 1, 1, 0, 0],
#                 [0, 0, 1, 0, 0, 1, 1],
#                 [0, 0, 1, 0, 0, 1, 1] ] )

# New example data
# data = array([ [1, 0, 1, 0, 1, 1, 0, 0, 0],
#                 [0, 1, 1, 0, 0, 0, 1, 0, 0],
#                 [1, 1, 1, 1, 0, 0, 0, 1, 0],
#                 [0, 0, 1, 1, 1, 0, 0, 0, 1],
#                 [1, 0, 0, 1, 1, 0, 0, 1, 0],
#                 [1, 0, 0, 0, 0, 1, 1, 0, 0],
#                 [0, 1, 0, 0, 0, 1, 1, 0, 0],
#                 [0, 0, 1, 0, 1, 0, 0, 1, 1],
#                 [0, 0, 0, 1, 0, 0, 0, 1, 1] ] )

# Generate random data (to test how long this will take on larger datasets)
data = random.randint(2, size=(1000, 1000))
print "Finished generating data."

eigenvalues,eigenvectors = linalg.eig(data)
print "Eigenvalues:"
print eigenvalues.round().astype(int)

print "Eigenvalues after absolute value:"
abs_eigenvalues = absolute(eigenvalues.round().astype(int))
print abs_eigenvalues

print "Principle Eigenvalue (largest):"
principle_eigenvalue = amax(abs_eigenvalues)
print principle_eigenvalue

print "Principle Eigenvalue Index:"
principle_index = where(abs_eigenvalues == principle_eigenvalue)[0][0]
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
for x in nditer(eigenvectors_index):
    normalized_eigenvectors.append(round(x * (1/sum_eig), 3))
print normalized_eigenvectors

print "Largest Gould Index:"
print amax(normalized_eigenvectors)

print "Smallest Gould Index:"
print amin(normalized_eigenvectors)

