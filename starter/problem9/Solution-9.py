my_list = [4, 8, 7, 6,4,3,2,1,9]
count=0
for i in range(len(my_list)):
    if my_list[i]==6:
        count+=1
if count>=1:
    print("6 is available")
else:
    print("6 is not available")