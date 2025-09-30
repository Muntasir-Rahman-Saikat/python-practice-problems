Input= ["ai", "ml", "python", "ml", "dl", "ai"]
def duplicates(s):
    x=[]
    duplicate=[]
    for i in s:
        if i in x:
            duplicate.append(i)
        else:
            x.append(i)
    print(duplicate)
duplicates(Input)

