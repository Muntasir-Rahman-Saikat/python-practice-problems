Input="Data Science is Awesome"

def vowel_numbers(s):
    vowels = ["a", "e", "i", "o", "u"]
    count=0
    for i in s.lower():
        if i in vowels:
            count+=1
    print(count)
vowel_numbers(Input)
