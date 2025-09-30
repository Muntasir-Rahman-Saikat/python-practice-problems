Input= 9875
def sum_of_digits_of_a_number(x):
    sum=0
    while(x>0):

        digit=x%10
        x=x//10
        sum+=digit
    print(sum)
sum_of_digits_of_a_number(Input)

def sum_of_digits_of_a_number_using_string(number):
    string=str(number)
    s=list(string)
    n=[int(i) for i in s]
    sums=sum(n)
    print(sums)
sum_of_digits_of_a_number_using_string(Input)

