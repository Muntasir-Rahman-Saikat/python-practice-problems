def func(a):
    if a%5==0 and a%3==0:
        return "FizzBuzz"
    elif a%5==0:
        return "Buzz"
    elif a%3==0:
        return "Fizz"
    else :
        return "Not a Fizz-buzz number"
print(func(23))