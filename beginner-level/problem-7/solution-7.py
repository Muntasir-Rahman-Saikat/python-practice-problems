Input=[1, 2, 4, 5]
def find_missing_number(x):
    sum_of_x=sum(x)
    n=max(x)
    total_sum=int(n*(n+1)/2)
    missing_number=total_sum-sum_of_x
    return missing_number
print(find_missing_number(Input))


