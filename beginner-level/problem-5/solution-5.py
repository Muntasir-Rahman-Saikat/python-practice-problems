Input =[1, [2, 3], [4, [5],(5,2)]]
def flattens(x):
    result=[]
    for values in x:
        if isinstance(values,(list,tuple)):
            result.extend(flattens(values))
        else:
            result.append(values)
    return result
print(flattens(Input))



