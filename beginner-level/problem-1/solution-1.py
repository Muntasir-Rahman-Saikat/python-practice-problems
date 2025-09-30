Input="bongodev"

def reverese_string(s):
    x = ""
    for i in range(len(s)-1,-1,-1):
        x+=s[i]
    print(x)
reverese_string(Input)
