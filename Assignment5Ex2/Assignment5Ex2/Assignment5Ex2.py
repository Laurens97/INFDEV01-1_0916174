pwd=raw_input("Please put in your password. It will be safe. Trust me.:\n")

wk="Your password is classified as weak."
med="Your password is classified as medium."
stn="Your password is classified as strong."

    #password length = 0 check
while (len(pwd)==0):
    pwd=raw_input("Invalid input. Please put in your password.:\n")

    #password 1->10 check
if (len(pwd)>=1 and len(pwd)<11):
    print wk

    #password 11->28 check
if (len(pwd)>=11 and len(pwd)<29):
    print med

    #password 29+ check
if (len(pwd)>=29):
    print stn