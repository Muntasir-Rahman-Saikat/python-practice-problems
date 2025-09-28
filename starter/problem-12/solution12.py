list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13]
new_list=[]
repeat=[]

for i in list1:
    if i in repeat:
        continue
    if i in list2:
        new_list.append(i)
    repeat.append(i)
print(new_list)
print(sum(new_list))
