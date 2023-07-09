from numpy import array ,linalg

#istema de dos ecuaciones y dos incognitas 
# x+2y=1
# 3x+5y=2

a=array([[1,2],[3,5]])
b= array([1,2])


print(linalg.solve(a,b))