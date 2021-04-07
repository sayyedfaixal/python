import math
def merge_sort(a, p, r):
    if (p<r):
        q= int(math.floor(p+r)/2)
        merge_sort(a,p, q)
        merge_sort(a, q+1, r)
        merge(a, p,q, r)
        # print(result)

def merge(a,p,q,r):
    left =[]
    right = []
    for i in range(p, q):
        left.append(a[i])

    for i in range(q+1, r):
        left.append(a[i])

    print(left)
    print(right)
    i =0
    j= 0
    # for _ in range(r):
    #     if(left[i]<=right[i]):
    #         a[i] = left[i]
    #         i+=1
    #     else:
    #         a[i] = right[i]
    #         j+=1
    print(a)
    
a = [12,343,23,2,12,53,13,14,543,234,542,432,54]
merge_sort(a, 0, 12)
print(a)