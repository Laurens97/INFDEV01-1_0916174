import os

    #defining clearing screen for Win, Linux & MacOSX
def cls():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

firsttxt=raw_input("Please input a string:\n")
cls()
num=raw_input("Please input a number:\n")
cls()

    #defining txt as list of firsttxt
txt=list(firsttxt)
print txt


    #defining x
x=len(txt)

while True:
    try:
        int(num)
        break
    except:
        num=raw_input("Wrong input. Please input a number:\n")
        cls()

#--------TESTING--------#
"""
y=x*(-1)
print y
print txt[y]
print ord(txt[y])
print int(ord(txt[y]))
print int(ord(txt[y]))+int(n)
print chr(int(ord(txt[y]))+int(n))+"\n"
"""
#--------TESTING--------#

while not x==0: 
    y=x*(-1)
    txtordint = int(ord(txt[y]))
    n=int(num)%26
    if (txtordint >= 65 and txtordint <= 90) or (txtordint >= 97 and txtordint <= 122):
        if ((txtordint+n) > 90 and txtordint >= 65 and txtordint <= 90) or (txtordint >= 97 and txtordint <= 122 and (txtordint+n) > 122):
            n-=26
        elif ((txtordint+n) < 65 and txtordint >= 65 and txtordint <= 90) or (txtordint >= 97 and txtordint <= 122 and (txtordint+n) < 97):
            n+=26
        txt[y] = chr((txtordint)+n)
    x-=1

cls()

newtxt = "".join(txt)
print "The string %s with a shift with a value of %s makes the following string:\n\n%s\n" %(firsttxt, num, newtxt)