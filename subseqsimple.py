def generate_subseq(s):
    subseq = ['']
    for char in s:
        new_subseq = []
        for subs in subseq:
            new_subseq.append(subs + char)
        subseq.extend(new_subseq)
    return subseq

string = 'abcd'
result = generate_subseq(string)
print("All subseq is ", string, "are:")
for subseq in result:
    print(f"'{subseq}'")