import re
def valid_email(email:str)->bool:
    pattern= r"^[\w\.-\]+@[\w]+[\.]+(\w+)$"
    return re.match(pattern,email) is not None
print(valid_email("muntasir6182@gmail.com"))