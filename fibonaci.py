def fibo(n):
    t1=0
    t2=1
    if(n==0 or n==1):
        print(n)
    else:
        for i in range(n):
            next_term = t1+t2
            print(next_term)
            t1=t2
            t2=next_term




n = int(input("Enter the number to find the fibonacii series upto that number :"))
fibo(n)