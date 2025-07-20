import re

def check_specialchars(input_str):
    pattern = r'[!]()#$@'

    if re.search(pattern,  input_str):
        return True
    else:
        return False


input_string = str(input("Enter a string"))
contains_spl = check_specialchars(input_string)
print(contains_spl)