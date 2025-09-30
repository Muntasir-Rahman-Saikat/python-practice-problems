Input= "python for web developers"
def capitalize_first_char(string):
    new_string_list= []

    for i in string.split(" "):
        new_string_list.append(i[0].upper()+i[1:].lower())
    new_string=" ".join(new_string_list)
    return new_string

print(capitalize_first_char(Input))

