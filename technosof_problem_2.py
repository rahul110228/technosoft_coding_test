from collections import defaultdict

input_data = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print("strs=" + str(input_data))

dict_temp = defaultdict(list)
for item in input_data:
    print(str(sorted(item)))
    print(item)
    dict_temp[str(sorted(item))].append(item)
group_anagrams = list(dict_temp.values())

print(str(group_anagrams))
