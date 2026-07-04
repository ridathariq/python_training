a = '23'
b = len(a)

dict = {
    '2':'abc',
    '3':'def'
}

collection = ['']
for i in  a:
    new = []
    c = dict[i]
    for j in c:
        for colls in collection:
            new.append(colls + j)
    collection = new
print(collection)
