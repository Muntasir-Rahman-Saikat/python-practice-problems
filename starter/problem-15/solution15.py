
lstudent_1 = [40, 35, 70, 90, 56]
student_2 = [57, 55, 80, 98, 46]
student_list={"lstduent_1":lstudent_1 ,"student_2":student_2 }
for i in student_list:
    fail = False
    for j in student_list[i]:
        if j<40:
            fail=True
    if not fail:
        x=sum(student_list[i])/(len(student_list[i]))
        print(f"avg is {x:.2f}")
    elif fail:
        print(f"{i} got failed")

