n=int(input())
fact =1
num = n
for i in range(1,n+1):
    fact=fact*num
    num-=1
print(fact)