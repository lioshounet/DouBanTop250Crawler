arr2 = ["1'","2'","3'","4'"]
arr3 = []

for arr in arr2:
    arr3.append(arr.replace("'", " "))

for arr in arr3:
    print(arr)
