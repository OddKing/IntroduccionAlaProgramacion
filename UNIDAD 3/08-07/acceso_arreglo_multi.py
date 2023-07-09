from numpy import array

a=array([[1,2,4],[4,5,6]])

print(a[1,0])
print(a[1][0])

print (a[1],[0])#no es igual

print(a[:,0:2])