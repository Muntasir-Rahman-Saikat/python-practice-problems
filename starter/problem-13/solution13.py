dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}
common_keys=dict1.keys() & dict2.keys()
common_items={key:(dict1[key],dict1[key]) for key in common_keys}
print(common_items)