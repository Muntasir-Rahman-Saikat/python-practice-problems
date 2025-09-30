input_text = "Madam"
input_text2 = "A sman, a plan, a canal, Panama"
def palindrome(x):
    p=x.replace(" ", "").replace(",", "").lower()
    left=0
    right= len(p) - 1
    same_char=True
    while left<right:
        if p[left]!=p[right]:
            same_char=False
            break
        else:
            left+=1
            right-=1
    if same_char:
        print("True")
    else:
        print("False")
palindrome(input_text2)

