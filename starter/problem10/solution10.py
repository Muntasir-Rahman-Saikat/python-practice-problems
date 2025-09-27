data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
age=[]
for i in range(len(data_list)):
    if type(data_list[i]) is int:
        age.append(data_list[i])
print(age)
