def facto(x):
    if x==1 or x==0:
        return 1
    else:
        return x*facto(x-1)

print(facto(5))