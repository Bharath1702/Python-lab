import re
def isphonenumber(numStr):
    if len(numStr) !=12:
        return False
    for i in range(len(numStr)):
        if i==3 or i ==7:
            if numStr[i] !="-":
                return False
            else:
                if numStr[i].isdigit()==False:
                    return False
    return True

def chkphonenumber(numStr):
    ph_no_pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match(numStr):
        return True
    else:
        return False
    
ph_num = input("enter the phone number")
print('without using regular expression')
if isphonenumber(ph_num):
    print("the phone number is valid")
else:
    print("invalid phone number")
print('using regular expression')
if chkphonenumber(ph_num):
    print("valid phone number")
else:
    print('Invalid phone number')
