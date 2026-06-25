arr1 = [2,3]
arr2 = [5,6,4]

merged = arr1 + arr2
unique = list(set(merged))
merged.sort()

print(unique)   
mid = len(merged)/2 != 0
mid = len(merged)//2 
if mid:
    median = (merged[mid-1] + merged[mid]) / 2
else:   
    median = merged[mid]    
print(median)