d = {}
n = int(input("Enter numbe of dictionary : "))
for i in range(n):
    k,v = input("Enter key and value Separated by space : ").split()
    d.update({k:v})
print(d)
for keys in d:
    d[keys] = int(d(keys))
print(d)