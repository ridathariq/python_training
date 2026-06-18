n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())
n = (n-(m/k)+(p/j))
if k==0 and j==0:
    print("invalid input")
elif(m%k !=0 // p%j != 0):
    n = n-1
    print(n)


