lst =  [ 3,1,4,2,7,9]
sorted_lst = sorted(lst)

start = 0
end = len(lst)-1
print(sorted_lst)
sum = 12
flag =0

i = len(sorted_lst)
while(start<end):
    if(sorted_lst[start]+sorted_lst[end]== sum):
        print(f'Sum found at index {start}-{end}')
        flag =1
        break
    elif(sorted_lst[start]+sorted_lst[end]>sum):
        end-=1
        i-=1
    elif(sorted_lst[start]+sorted_lst[end]<sum):
        start+=1
        i-=1

if(flag==0):
    print("Required Sum cannot be found from the given array")

